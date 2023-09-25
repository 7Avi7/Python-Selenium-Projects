import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
achains = ActionChains(driver)

# Right Click

right_click = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
copy_element = driver.find_element(By.XPATH,"//li[@class='context-menu-item context-menu-icon context-menu-icon-copy']")
achains.context_click(right_click).perform()
time.sleep(2)
copy_element.click()
time.sleep(2)

# Accept Alert
Alert(driver).accept()
time.sleep(1)

# Double Click

double_click_ = driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")
achains.double_click(double_click_).perform()

# Accept Alert
Alert(driver).accept()

time.sleep(5)


driver.quit()
