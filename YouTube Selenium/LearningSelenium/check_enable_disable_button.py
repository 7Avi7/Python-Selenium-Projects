from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://training.openspan.com/login")

check_button = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()

print(check_button)

time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys('avilash')
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys('12345678')
time.sleep(2)


check_button2 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()

print(check_button2)


driver.find_element(By.XPATH, "//input[@id='login_button']").click()

time.sleep(2)


driver.quit()

