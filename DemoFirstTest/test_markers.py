import pytest
from selenium import webdriver
from  selenium.webdriver.common.by import By

pytestmark= [pytest.mark.regression, pytest.mark.e2e]
# pytestmark = pytest.mark.regression

@pytest.mark.smoke
def test_form_submission():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    driver.find_element(By.ID, "user-message").send_keys("marker conditions")
    driver.find_element(By.ID, "showInput").click()
    validate_msg = driver.find_element(By.ID, "message").text
    assert validate_msg.__contains__("marker")
    driver.quit()

def test_login():
    print("Login test")

@pytest.mark.sanity
def test_logout():
    print("Log out test")

@pytest.mark.smoke
def test_logs():
    print("test logs")

