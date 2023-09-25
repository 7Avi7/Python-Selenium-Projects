from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

# Find the email input field using XPath
email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='login-input']"))).send_keys("avi@x.com")


# Wait for 6 seconds
time.sleep(6)

# Close the browser
driver.quit()
