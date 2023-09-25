import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome()

# Cokiees=============
driver.get("https://eticket.railway.gov.bd/")
time.sleep(1)
driver.find_element(By.XPATH, "//body[1]/div[1]/div[9]/div[1]/div[2]/div[2]/button[1]").click()
time.sleep(1)

# Station from=============
# from_ = driver.find_element(By.XPATH, "//input[@id='dest_from']")
# from_.click()
# from_.send_keys('Dhaka')


# Find the search input element
search_input = driver.find_element(By.XPATH, "//input[@id='dest_from']")
# Enter the search query
search_query = "dhaka"
search_input.send_keys(search_query)

# Wait for the suggestion dropdown to appear (adjust the timeout as needed)
wait = WebDriverWait(driver, 5)  # Wait up to 10 seconds for the dropdown to appear
suggestion_dropdown = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Dhaka")))

# Find the desired suggestion element (e.g., the first suggestion)
suggestion_element = driver.find_element(By.XPATH, "//a[@id='ui-id-5']")  # Replace with the correct XPath or CSS selector for the suggestion item

# Click on the suggestion
suggestion_element.click()


# listelements = driver.find_element(By.XPATH,"//li//a[@id='ui-id-13']//div")
#
# for i in listelements:
#     if i.text == 'Dhaka':
#         i.click()
#         break


time.sleep(1)


# Class seat==========
select = Select(driver.find_element(By.ID, "choose_class"))

select.select_by_index(1)
time.sleep(2)
# select by visible text
select.select_by_visible_text('AC_B')

# select by value
select.select_by_value('F_CHAIR')
time.sleep(2)

# Calendar Date==========
driver.find_element(By.XPATH, "//input[@id='doj']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[normalize-space()='27']").click()
time.sleep(1)

driver.quit()
