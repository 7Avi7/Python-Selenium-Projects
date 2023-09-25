import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver= webdriver.Chrome()
driver.maximize_window()

# Navigate to the webpage
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Find all links with the specified CSS selector
links = driver.find_elements(By.CSS_SELECTOR, "li.gf-li a")

# Create an empty list to store the broken links
broken_links = []

for link in links:
    url = link.get_attribute("href")

    # Send an HTTP HEAD request to the URL
    response = requests.head(url)

    # Check the response code
    if response.status_code >= 400:
        print(f"The Link With Text '{link.text}' is broken with code {response.status_code}")
        broken_links.append(link.text)

# Check if any broken links were found
if broken_links:
    print("Broken links found:")
    for link_text in broken_links:
        print(link_text)
else:
    print("No broken links found")

class TestBrokenLinks(unittest.TestCase):

    def setUp(self):
        # Create a WebDriver instance (you'll need to specify the path to your Chrome WebDriver executable)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_broken_links(self):
        # Navigate to the webpage
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")

        # Find all links with the specified CSS selector
        links = self.driver.find_elements(By.CSS_SELECTOR, "li.gf-li a")

        # Iterate through the links and perform checks
        for link in links:
            url = link.get_attribute("href")

            # Send an HTTP HEAD request to the URL
            response = requests.head(url)

            # Get the response code
            response_code = response.status_code
            print(response_code)

            # Check the response code and log any failures
            self.assertTrue(response_code < 400, f"The Link With Text '{link.text}' is broken with code {response_code}")

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()



# Close the WebDriver
driver.quit()
