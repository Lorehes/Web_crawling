from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))
USERNAME = os.getenv("id")
PASSWORD = os.getenv("pw")

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists and is compatible with the installed Chrome browser. If not, it will download and install the latest version.

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")  # Hide automation flag
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Remove automation banner
options.add_experimental_option("useAutomationExtension", False)  # Disable automation extension

driver = webdriver.Chrome(options=options)  # Create a new instance of the Chrome driver
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")  # Hide webdriver property

def login(driver, username, password):
    driver.get("https://www.instagram.com/accounts/login/")  # Open the login page
    time.sleep(5)  # Wait for login form to render
    input_id = driver.find_element(By.NAME, "email")  # Find the username input field
    input_id.click()  # Focus the input field
    input_id.send_keys(username)  # Enter the username
    input_pw = driver.find_element(By.NAME, "pass")  # Find the password input field
    input_pw.click()  # Focus the input field
    input_pw.send_keys(password)  # Enter the password
    input_pw.send_keys(Keys.RETURN)  # Submit the form by pressing Enter
    time.sleep(10)  # Wait for login to complete
    
# search
def search_hashtag(driver, hashtag):
    url = f'https://www.instagram.com/explore/tags/{hashtag}/'  # URL of the Instagram search page for the hashtag
    driver.get(url=url)  # Open the Instagram search page
    time.sleep(10)  # Wait for page to load
    
# scroll
def scroll_page(driver, times):
    for _ in range(times):  # Scroll down specified number of times
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll to the bottom of the page
        time.sleep(5)  # Wait for new content to load
        
        
def like_comments(driver):
    # Placeholder for liking comments functionality
    pass


login(driver, USERNAME, PASSWORD)
hashtag = "인스타그램"  # Hashtag to search for
search_hashtag(driver, hashtag)
scroll_page(driver, 5)
like_comments(driver)
time.sleep(299)  # Wait for login to complete
