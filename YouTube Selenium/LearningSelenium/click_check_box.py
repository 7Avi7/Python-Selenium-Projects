from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Create a WebDriver instance (e.g., Chrome or Firefox)
driver = webdriver.Chrome()

# Navigate to the desired URL
driver.get("https://designsystem.digital.gov/components/checkbox/")

driver.find_element(By.XPATH,"//label[@for='check-historical-douglass']").click()

time.sleep(6)


# Close the browser window
driver.quit()
