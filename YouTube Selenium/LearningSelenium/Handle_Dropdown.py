import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft')

select = Select(driver.find_element(By.NAME,'UserTitle'))

select.select_by_index(1)
time.sleep(5)
# select by visible text
select.select_by_visible_text('Sales Manager')

# select by value
select.select_by_value('Marketing_PR_Manager_ANZ')
time.sleep(2)