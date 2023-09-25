from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.rcvacademy.com/")

elements_list = driver.find_elements(By.TAG_NAME, "a")

# Print the list of elements
for element in elements_list:
    print(element.text)

# Get the length of the list and print it
list_length = len(elements_list)
print(f"Number of elements in the list: {list_length}")


time.sleep(1)
driver.maximize_window()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Login").click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
driver.refresh()
time.sleep(2)
driver.minimize_window()
time.sleep(5)
driver.quit()

