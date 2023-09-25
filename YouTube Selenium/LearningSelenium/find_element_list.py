from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Create ChromeOptions object to configure the browser settings
chrome_options = Options()

# Add argument to disable sandbox
chrome_options.add_argument("--no-sandbox")

# Start Chrome with the configured options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the Yatra website
driver.get("https://www.yatra.com")

# Find all the elements with a specific CSS selector, for example, "a" (anchors/links)
elements_list = driver.find_elements(By.TAG_NAME, "a")

# Print the list of elements
for element in elements_list:
    print(element.text)

# Get the length of the list and print it
list_length = len(elements_list)
print(f"Number of elements in the list: {list_length}")

# Close the browser
driver.quit()
