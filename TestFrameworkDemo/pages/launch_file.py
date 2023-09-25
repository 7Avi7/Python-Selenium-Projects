import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class LaunchPage:
    def __init__(self, driver):
        self.driver = driver

    def test_drag_and_drop(self, driver):
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

        elem1 = driver.find_element(By.ID, "draggable")
        elem2 = driver.find_element(By.ID, "droppable")

        # Scroll to elem1 to make it visible
        driver.execute_script("arguments[0].scrollIntoView();", elem1)

        # Scroll to elem2 to make it visible
        driver.execute_script("arguments[0].scrollIntoView();", elem2)

        # Drag and drop elem1 to elem2
        ActionChains(driver).drag_and_drop(elem1, elem2).perform()

        # Drag and drop elem1 by an offset (100 pixels to the right, 100 pixels down)
        ActionChains(driver).drag_and_drop_by_offset(elem1, 100, 100).perform()
        time.sleep(4)

        # Assertion to check if the drop was successful
        assert elem2.text == "Dropped!"
