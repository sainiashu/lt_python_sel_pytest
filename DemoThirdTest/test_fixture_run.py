from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

driver = webdriver.Chrome()

@pytest.fixture(autouse=True)
def verify_fixture_condition():
    print("Pytest Fixture Auto use condition is working fine")

@pytest.fixture(scope="function")
def setup_teardown():
    driver.get("https://demowebshop.tricentis.com/login")
    driver.find_element(By.CSS_SELECTOR, "#Email").send_keys("Demo1.Tester@test.test")
    driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("Tester@123")
    driver.find_element(By.XPATH,"//input[@value='Log in']").click()
    print("Login Successful")

    yield

    driver.find_element(By.XPATH, "//a[@class='ico-logout']").click()
    print("Log Out Successful")

@pytest.mark.usefixtures("setup_teardown")
def test1_navigate_book_page():
    driver.find_element(By.XPATH,"//li[@class='inactive']//a[normalize-space()='Books']").click()
    page_title =driver.find_element(By.XPATH,"//h1[normalize-space()='Books']").text
    assert "Books" in page_title
    print("Test 1 is complete")

@pytest.mark.usefixtures("setup_teardown")
def test2_navigate_gift_card_page():
    driver.find_element(By.XPATH,"//li[@class='inactive']//a[normalize-space()='Gift Cards']").click()
    page_content =driver.find_element(By.XPATH,"//h1[normalize-space()='Gift Cards']").text
    assert "Gift Cards" in page_content
    print("Test 2 is complete")
