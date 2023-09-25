import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
# driver.get("https://training.rcvacademy.com/")

driver.execute_script("window.open('https://training.rcvacademy.com/', '_self');")
time.sleep(2)
demo_element = driver.execute_script("return document.getElementsByTagName('a')[5];")
driver.execute_script("arguments[0].click();", demo_element)

driver.quit()