import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class run(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_LaunchBrowser(self):
        # Go To the url
        self.driver.get("https://www.munchies.com.bd")

    def test_searchLocation(self):
        # From Location
        self.driver.get("https://www.munchies.com.bd")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter your current area, ex: Gulshan']").send_keys(
            'bashundhara r/a')
        time.sleep(5)
        location = self.driver.find_elements(By.XPATH,"//div[@class='text-black text-sm md:text-base lg:text-lg font-medium tracking-wide flex justify-between hover:cursor-pointer hover:bg-slate-300 p-2 rounded-lg']")
        time.sleep(5)
        print("Total suggestions are: ", len(location))

        for i in location:
            print("Suggestions are: ", i.text)
            if i.text == 'bashundhara r/a':
                print("Record found")
                i.click()
                break
        time.sleep(5)
        # self.driver.find_elements(By.LINK_TEXT,"Log in").click();
        # time.sleep(5)
        # self.driver.get("https://www.munchies.com.bd/login")
    # def test_ScrollHomePage(self):
    #     self.driver.get("https://www.munchies.com.bd")
    #
    #     # Scroll
    #     def scroll_down():
    #         # Scroll down the page by 50 pixels
    #         self.driver.execute_script("window.scrollBy(0, 50);")
    #         # time.sleep(5)  # Optional: Add a small delay to let the page load
    #         # Perform the scrolling multiple times (change the range as needed)
    #         for i in range(2):  # This will scroll down 5 times
    #             scroll_down()
    #         time.sleep(2)

    def test_ClickLoginPage(self):
        # From Location
        self.driver.get("https://www.munchies.com.bd")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter your current area, ex: Gulshan']").send_keys(
            'bashundhara r/a')
        time.sleep(5)
        location = self.driver.find_elements(By.XPATH,
                                             "//div[@class='text-black text-sm md:text-base lg:text-lg font-medium tracking-wide flex justify-between hover:cursor-pointer hover:bg-slate-300 p-2 rounded-lg']")
        time.sleep(5)
        print("Total suggestions are: ", len(location))

        for i in location:
            print("Suggestions are: ", i.text)
            if i.text == 'bashundhara r/a':
                print("Record found")
                i.click()
                break
        time.sleep(5)
        self.driver.refresh()
        self.driver.get("https://www.munchies.com.bd/login")
        # self.driver.get("https://www.munchies.com.bd/")
        # self.driver.find_element(By.XPATH, "//a[normalize-space()='Log in']").click()
        # self.driver.refresh()
        # self.driver.find_element(By.LINK_TEXT, "Log in").click()
        time.sleep(2)
        #
        self.driver.find_element(By.XPATH, "//input[@id=':r2:']").send_keys("01998946020")

        time.sleep(2)

        self.driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()

        time.sleep(4)
    def test_overallResults(self):
        # From Location
        self.driver.get("https://www.munchies.com.bd")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter your current area, ex: Gulshan']").send_keys(
            'bashundhara r/a')
        time.sleep(5)
        location = self.driver.find_elements(By.XPATH,
                                             "//div[@class='text-black text-sm md:text-base lg:text-lg font-medium tracking-wide flex justify-between hover:cursor-pointer hover:bg-slate-300 p-2 rounded-lg']")
        time.sleep(5)
        print("Total suggestions are: ", len(location))

        for i in location:
            print("Suggestions are: ", i.text)
            if i.text == 'bashundhara r/a':
                print("Record found")
                i.click()
                break
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Log in']").click()
        self.driver.find_element(By.XPATH, "//input[@id=':r2:']").send_keys("01998946020")

        time.sleep(2)

        self.driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()