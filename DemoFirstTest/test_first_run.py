from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def test_selenium_playground():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/")
    print("Title: " , driver.title)
    driver.quit()

def test_lambda_ecom():
    driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    print("Title: ", driver.title)
    driver.quit()