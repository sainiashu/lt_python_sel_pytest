from datetime import datetime

import pytest
from selenium import webdriver

class TestLambdaTest:
    def test_sample_app_title(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
        pytest.skip()

@pytest.mark.skip(reason="Feature is not ready for testing")
def test_ecom(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://demowebshop.tricentis.com/")

@pytest.mark.skip()
def test_2(self):
    print("Check skip case")

@pytest.mark.skipif(datetime.now() <= datetime(2099,12,11), reason="feature will not develop")
def test_skip_if():
    driver = webdriver.Chrome()
    driver.get("https://www.lambdatest.com/certifications/selenium-python-101")

