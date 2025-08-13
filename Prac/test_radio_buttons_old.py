from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
from webdriver_manager.chrome import ChromeDriverManager

from conftest import access_token

user_name= "sainiashu90"
access_key = "LT_Mq3U2dNlRNaOtTubDs8OiI3aw5HWN90QqgfbcnuRlHhLKiL"

capabilities ={
    "browserName":  "Chrome",
    "browserVersion": "121.0",
    "platformName": "Windows 11",
    "selenium_version": "4.0.0"
}

driver = webdriver.Remote(
    command_executor="http://{user_name}:{access_key}@hub.lambdatest.com/wd/hub",
    desired_capabilities=capabilities
)


def test_verify_radio_btn_checked():
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.lambdatest.com/selenium-playground")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//a[normalize-space()='Radio Buttons Demo']").click()
    driver.find_element(By.CSS_SELECTOR,"input[value='Male'][name='optradio']").click()
    driver.find_element(By.ID, "buttoncheck").click()

    # actual_text =driver.find_element(By.XPATH, "//p[@class='text-gray-900 text-size-15 my-10 text-black radiobutton']").text
    actual_text = driver.find_element(By.CSS_SELECTOR,"[id='buttoncheck']~p").text

    assert "Male" in actual_text
    driver.save_screenshot("RadioButton_Demo.png")
    driver.quit()
