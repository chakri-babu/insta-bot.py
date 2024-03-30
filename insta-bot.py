from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import random

def initialize_driver():
    options = Options()
    options.headless = True  # Run in headless mode
    options.add_argument("--no-sandbox")  # Bypass the sandbox environment
    options.add_argument("--disable-dev-shm-usage")  # Disable shared memory usage
    options.add_argument("--disable-gpu")  # Disable GPU acceleration
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--mute-audio")  # Mute audio
    # Set user-agent to mimic a mobile device
    user_agent = "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")
    return webdriver.Firefox(options=options)

def login(driver, username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(random.uniform(2, 4))
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector("button[type='submit']").click()
    time.sleep(random.uniform(4, 6))
    try:
        driver.find_element_by_xpath("//button[text()='Not Now']").click()
        time.sleep(random.uniform(2, 3))
    except NoSuchElementException:
        pass

def send_follow_requests(driver, num_requests):
    driver.get("https://www.instagram.com/explore/people/")
    time.sleep(random.uniform(2, 4))
    for _ in range(num_requests):
        try:
            random_user = driver.find_element_by_xpath("//button[text()='Follow']")
            random_user.click()
            time.sleep(random.uniform(3, 5))
            print("Follow request sent")
        except NoSuchElementException:
            print("No more users to follow")
            break

if __name__ == "__main__":
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    num_requests = int(input("Enter the number of follow requests to send: "))

    try:
        driver = initialize_driver()
        login(driver, username, password)
        send_follow_requests(driver, num_requests)
    finally:
        driver.quit()
