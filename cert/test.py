import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.client_config import ClientConfig
import os

# Get LambdaTest credentials from Gitpod environment variables
USER_NAME = os.getenv("LT_USERNAME")
ACCESS_KEY = os.getenv("LT_ACCESS_KEY")

if not USER_NAME or not ACCESS_KEY:
    raise ValueError("LambdaTest credentials not found. Please set LT_USERNAME and LT_ACCESS_KEY in Gitpod.")

caps = {
    "browserName": "Chrome",
    "browserVersion": "121.0",
    "platformName": "Windows 11",
    "selenium_version": "4.0.0"
}

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.set_capability("LT:Options", caps)

    # Secure ClientConfig with credentials from environment
    client_config = ClientConfig(
        remote_server_addr="https://hub.lambdatest.com/wd/hub",
        username=USER_NAME,
        password=ACCESS_KEY
    )

    driver = webdriver.Remote(
        command_executor="https://hub.lambdatest.com/wd/hub",
        options=options,
        client_config=client_config
    )

    yield driver
    driver.quit()

def test_radio_btn(driver):
    driver.get("https://www.lambdatest.com/selenium-playground/")
    driver.maximize_window()

    radio_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Radio Buttons Demo"))
    )
    radio_link.click()

    driver.find_element(By.CSS_SELECTOR, "input[value='Male'][name='optradio']").click()
    driver.find_element(By.ID, "buttoncheck").click()

    actual_text = driver.find_element(By.CSS_SELECTOR, "[id='buttoncheck']~p").text
    assert "Male" in actual_text

    driver.save_screenshot("RadioButton_Demo.png")
