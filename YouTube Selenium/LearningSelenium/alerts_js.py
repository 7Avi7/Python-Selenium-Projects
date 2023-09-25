import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_prompt")
driver.maximize_window()
driver.switch_to.frame("iframeResult")
# Accept Alert
# driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
# time.sleep(1)
# driver.switch_to.alert.accept()
# time.sleep(1)

# Dissmiss Alert

# driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
# time.sleep(1)
# driver.switch_to.alert.dismiss()
# time.sleep(1)

# Send Text Alert

driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
# time.sleep(1)
driver.switch_to.alert.send_keys("Hello Avi..!")
Alert(driver).accept()
time.sleep(5)

driver.quit()