from selenium import webdriver
from selenium.webdriver.common.by import By


def test_search_items():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.find_element(By.CSS_SELECTOR, "div[id='entry_217822'] input[placeholder='Search For Products']").send_keys("iphone")
    driver.find_element(By.CSS_SELECTOR, "button[class='type-text']").click()
    search_item = driver.find_element(By.CSS_SELECTOR,"h1[class='h4']").text

    assert "iphone" in search_item
    driver.quit()