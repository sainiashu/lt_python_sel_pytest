from  selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("driver_initialization")
class BaseClass:
    pass

class Test_SeleniumGrid(BaseClass):
    def test_check_boxes(self):
        driver = webdriver.Chrome()
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "//li[@class='inactive']//a[normalize-space()='Electronics']").click()
        # page_title = driver.title
        # assert "electronics" in page_title