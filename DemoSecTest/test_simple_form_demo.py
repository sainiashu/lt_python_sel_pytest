from selenium import webdriver
from  selenium.webdriver.common.by import By

def test_web_form():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    driver.find_element(By.ID, "user-message").send_keys("Learning")
    driver.find_element(By.ID,"showInput").click()
    validate_msg = driver.find_element(By.ID,"message").text

    assert "Learning" in validate_msg

    driver.quit()

def test_web_form2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    driver.find_element(By.ID, "user-message").send_keys("argument k")
    driver.find_element(By.ID,"showInput").click()
    validate_msg = driver.find_element(By.ID,"message").text

    assert "argument k" in validate_msg

    driver.quit()