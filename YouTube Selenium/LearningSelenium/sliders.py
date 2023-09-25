import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.codehim.com/demo/wrunner-html-range-slider-with-2-handles/")
driver.maximize_window()
time.sleep(8)


left_slider = driver.find_element(By.XPATH, "//div[contains(@class,'my-js-slider')]//div[@class='wrunner__path wrunner__path_theme_default wrunner__path_direction_horizontal']//div[1]")
right_slider = driver.find_element(By.XPATH, "//div[contains(@class,'my-js-slider')]//div[@class='wrunner__path wrunner__path_theme_default wrunner__path_direction_horizontal']//div[1]")

ActionChains(driver).drag_and_drop_by_offset(left_slider, 10, 0).perform()

ActionChains(driver).drag_and_drop_by_offset(right_slider, -10, 0).perform()

time.sleep(2)

driver.quit()
