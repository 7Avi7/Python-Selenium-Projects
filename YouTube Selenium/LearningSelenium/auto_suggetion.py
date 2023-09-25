import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://google.com')

search = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
time.sleep(2)
search.click()
time.sleep(2)
search.send_keys('peoplentech')
time.sleep(2)
search.send_keys(Keys.ENTER)

time.sleep(5)  # Adding a sleep to wait for the search results to load
driver.quit()
