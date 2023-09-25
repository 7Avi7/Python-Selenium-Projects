from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")

check_show = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
print(check_show)


driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()

check_show2 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
print(check_show2)



driver.quit()

