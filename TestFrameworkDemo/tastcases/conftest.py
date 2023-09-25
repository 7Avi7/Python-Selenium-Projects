import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()  # Change to your desired webdriver (e.g., Firefox, Safari, etc.)
    driver.get("https://jqueryui.com/droppable/")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
