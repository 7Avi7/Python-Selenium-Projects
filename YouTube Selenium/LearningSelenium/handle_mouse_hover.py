import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.rcvacademy.com/")
driver.maximize_window()

tutorials = driver.find_element(By.XPATH, "//a[normalize-space()='Tutorials']")
about = driver.find_element(By.XPATH, "//a[@href='http://rcvacademy.com/about-us/']")
automation_testing = driver.find_element(By.XPATH,"//li[@id='menu-item-11921']//a[normalize-space()='Automation Testing']")

achains = ActionChains(driver)

# About
achains.move_to_element(about).perform()
time.sleep(3)

# Tutorial
achains.move_to_element(tutorials).perform()
time.sleep(3)
achains.move_to_element(automation_testing).perform()
time.sleep(3)
driver.find_element(By.XPATH, "//a[normalize-space()='Selenium Cucumber BDD Tutorial']").click()
time.sleep(3)

driver.quit()
