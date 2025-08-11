from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest

@pytest.mark.parametrize("num1,num2,expected_result",
                         [
                             ("10","20","30"),
                             ("30","20","50"),
                             ("5","5","30"),
                         ])

def test_parameter(num1,num2,expected_result):
    driver = webdriver.Chrome()
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//input[@id='sum1']").send_keys(num1)
    driver.find_element(By.XPATH,"//input[@id='sum2']").send_keys(num2)
    driver.find_element(By.XPATH,"//button[normalize-space()='Get Sum']").click()
    actual_total =driver.find_element(By.XPATH,"//p[@id='addmessage']").text

    assert actual_total == expected_result,\
        "Actual vs Expected values does not match"
    driver.quit()
