import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.test_data import TestData


@pytest.fixture(params=["chrome","firefox"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif request.param == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    # elif request.param == "edge":
    #     # driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    request.cls.driver = driver
    print("Browser: ", request.param)
    driver.get(TestData.url)
    driver.maximize_window()
    yield
    print("Close Driver")
    driver.close()