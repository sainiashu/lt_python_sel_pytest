import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("initialize_driver")
class BaseClass:
    pass

class Test_Drivers(BaseClass):
    def test_multiple_browsers(self):
        self.driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
        header_text=self.driver.find_element(By.CSS_SELECTOR, "[class='wrapper'] h1").text
        print("Header: ", header_text)
        assert header_text == "Simple Form Demo"
