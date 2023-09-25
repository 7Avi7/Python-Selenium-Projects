import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://chercher.tech/practice/practice-dropdowns-selenium-webdriver')

select = Select(driver.find_element(By.XPATH,"//select[@id='second']"))

select.select_by_index(1)

select.select_by_visible_text('Pizza')
select.select_by_value('Donut')
time.sleep(5)


select.select_by_index(3)

select.select_by_value('Bonda')

time.sleep(5)

driver.quit()