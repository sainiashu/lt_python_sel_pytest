import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.mark.parametrize("browser",["chrome","firefox"])
@pytest.mark.parametrize("url",["https://www.lambdatest.com/selenium-playground/simple-form-demo",
                                    "https://demowebshop.tricentis.com/"]
                                    )
def test_open_browser(browser,url):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(url)
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get(url)
    else:
        raise ValueError("Browser not supported")

    driver.maximize_window()

    driver.quit()


