from selenium import webdriver
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists and is compatible with the installed Chrome browser. If not, it will download and install the latest version.

driver = webdriver.Chrome()  # Create a new instance of the Chrome driver
driver.implicitly_wait(3)  # Wait for elements to load for up to 3 seconds

url = "https://www.instagram.com/"  # URL of the Instagram
driver.get(url)  # Open the Instagram website

time.sleep(20)  # Wait for 20 seconds to see the opened page