import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class Run(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_LaunchBrowser(self):
        self.driver.get("https://eticket.railway.gov.bd/")

    def test_AllScenarios(self):
        # Agreement
        self.driver.get("https://eticket.railway.gov.bd/")
        time.sleep(5)
        agreement_button = self.driver.find_element(By.XPATH,
                                                    "//body/div[@id='main_wrapper']/div[9]/div[1]/div[2]/div[2]/button[1]")
        agreement_button.click()
        time.sleep(5)
    #     From
    #     self.driver.get("https://eticket.railway.gov.bd/")
        from_station = self.driver.find_element(By.XPATH, "//input[@id='dest_from']")
        from_station.send_keys('Dhaka')
        time.sleep(2)  # Add a short delay to allow suggestions to load
        from_station.send_keys(Keys.RETURN)
        # To
        # self.driver.get("https://eticket.railway.gov.bd/")
        to_station = self.driver.find_element(By.XPATH, "//input[@id='dest_to']")
        to_station.send_keys('B Sirajul Islam')
        time.sleep(2)  # Add a short delay to allow suggestions to load
        to_station.send_keys(Keys.RETURN)
        # Calender
        # self.driver.get("https://eticket.railway.gov.bd/")
        time.sleep(5)
        date_picker = self.driver.find_element(By.XPATH, "//input[@id='doj']")
        date_picker.click()
        date_select = self.driver.find_element(By.XPATH, "//a[normalize-space()='15']")
        date_select.click()
        time.sleep(5)
        # Seat Class
        # self.driver.get("https://eticket.railway.gov.bd/")
        select_class = Select(self.driver.find_element(By.XPATH, "//select[@id='choose_class']"))
        select_class.select_by_index(2)
        # Search Train
        # self.driver.get("https://eticket.railway.gov.bd/")
        search_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Search Trains')]")
        actions = ActionChains(self.driver)
        actions.move_to_element(search_button).click().perform()
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)

        # self.driver.get("https://eticket.railway.gov.bd/booking/train/search/en?fromcity=Dhaka&tocity=B%20Sirajul%20Islam&doj=03-Sep-2023&class=AC_S")

        def test_method7(self):

            # Scroll
            # Function to scroll down the page
            def scroll_down():
                # Scroll down the page by 50 pixels
                self.driver.execute_script("window.scrollBy(0, 50);")
                time.sleep(5)  # Optional: Add a small delay to let the page load

            # Perform the scrolling multiple times (change the range as needed)
            for i in range(5):  # This will scroll down 5 times
                scroll_down()

    # def test_Agreement(self):
    #     self.driver.get("https://eticket.railway.gov.bd/")
    #     time.sleep(5)
    #     agreement_button = self.driver.find_element(By.XPATH, "//body/div[@id='main_wrapper']/div[9]/div[1]/div[2]/div[2]/button[1]")
    #     agreement_button.click()
    #     time.sleep(5)
    def test_From(self):
        self.driver.get("https://eticket.railway.gov.bd/")
        from_station = self.driver.find_element(By.XPATH, "//input[@id='dest_from']")
        from_station.send_keys('Dhaka')
        time.sleep(2)  # Add a short delay to allow suggestions to load
        from_station.send_keys(Keys.RETURN)  # Select the first suggestion

    def test_To(self):
        self.driver.get("https://eticket.railway.gov.bd/")
        to_station = self.driver.find_element(By.XPATH, "//input[@id='dest_to']")
        to_station.send_keys('B Sirajul Islam')
        time.sleep(2)  # Add a short delay to allow suggestions to load
        to_station.send_keys(Keys.RETURN)  # Select the suggestion

    def test_Calender(self):
        self.driver.get("https://eticket.railway.gov.bd/")
        time.sleep(5)
        date_picker = self.driver.find_element(By.XPATH, "//input[@id='doj']")
        date_picker.click()
        date_select = self.driver.find_element(By.XPATH, "//a[normalize-space()='3']")
        date_select.click()
        time.sleep(5)

    def test_SeatClass(self):
        self.driver.get("https://eticket.railway.gov.bd/")
        select_class = Select(self.driver.find_element(By.XPATH, "//select[@id='choose_class']"))
        select_class.select_by_index(2)  # Change the index to your desired class

    def test_SearchTrain(self):
        self.driver.get("https://eticket.railway.gov.bd/")
        search_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Search Trains')]")
        actions = ActionChains(self.driver)
        actions.move_to_element(search_button).click().perform()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)  # Add a delay to allow the search results to load




    @classmethod
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
