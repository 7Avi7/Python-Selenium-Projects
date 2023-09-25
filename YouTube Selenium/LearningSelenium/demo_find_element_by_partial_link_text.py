from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://www.yatra.com/")

driver.find_element(By.PARTIAL_LINK_TEXT, "Holiday").click()

# You can now interact with the new page as needed.

# Don't forget to close the browser when you're done with it.
driver.quit()
