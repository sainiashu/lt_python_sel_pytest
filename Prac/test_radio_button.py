import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()
USER_NAME = os.getenv("LT_USERNAME","")
ACCESS_KEY= os.getenv("LT_ACCESS_KEY","")

caps = {
    "browserName":  "Chrome",
    "browserVersion":   "121.0",
    "platformName": "Windows 11",
    "selenium_version": "4.0.0"
}

@pytest.fixture(scope="session")
def driver():
    options= Options()
    options.set_capability("LT:Options",caps)
    driver = webdriver.Remote(
        # command_executor="http://"+ USER_NAME + ":" + ACCESS_KEY + "@hub.lambdatest.com/wd/hub",
        command_executor=f"https://{USER_NAME}:{ACCESS_KEY}@hub.lambdatest.com/wd/hub",
        options=options
    )

    yield driver

    driver.quit()

def test_radio_btn(driver):
    driver.get("https://www.lambdatest.com/selenium-playground/")
    driver.maximize_window()

    male_radio_btn= WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Radio Buttons Demo']")))

    male_radio_btn.click()

    driver.find_element(By.CSS_SELECTOR, "input[value='Male'][name='optradio']").click()
    driver.find_element(By.ID, "buttoncheck").click()
    actual_text = driver.find_element(By.CSS_SELECTOR, "[id='buttoncheck']~p").text

    assert "Male" in actual_text
    driver.save_screenshot("RadioButton_Demo.png")
