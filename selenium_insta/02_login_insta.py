from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))
USERNAME = os.getenv("id")
PASSWORD = os.getenv("pw")

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists and is compatible with the installed Chrome browser. If not, it will download and install the latest version.

# options = webdriver.ChromeOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")  # Hide automation flag
# options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Remove automation banner
# options.add_experimental_option("useAutomationExtension", False)  # Disable automation extension

# driver = webdriver.Chrome(options=options)  # Create a new instance of the Chrome driver
# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")  # Hide webdriver property

url = "https://www.instagram.com/accounts/login/"  # Direct login URL
driver.get(url)  # Open the Instagram website

time.sleep(5)  # Wait for login form to render
input_id = driver.find_element(By.NAME, "email")  # Find the username input field
input_id.click()  # Focus the input field
input_id.send_keys(USERNAME)  # Enter the username

input_pw = driver.find_element(By.NAME, "pass")  # Find the password input field
input_pw.click()  # Focus the input field
input_pw.send_keys(PASSWORD)  # Enter the password
time.sleep(20)  # Wait for 20 seconds to see the opened page
