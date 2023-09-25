import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
continue_ = driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
continue_.screenshot(".testq.png")
continue_.click()
time.sleep(2)
driver.get_screenshot_as_file("D:\Python Selenium Projects\YouTube Selenium\error1.png")
driver.save_screenshot(".test1.png")
driver.save_screenshot("D:\Python Selenium Projects\YouTube Selenium\error12.png")



driver.quit()
