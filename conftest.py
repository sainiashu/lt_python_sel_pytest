import pytest
from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.remote.remote_connection import RemoteConnection

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.remote_connection import RemoteConnection

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



# Step One: Declares variables for setting up the selenium Grid test
user_name= "username"
access_token= "saved location"
remote_url = "http://" + user_name + ":" + access_token +"@hub.lambdatest.com/wd/hub"

#Step Two: Define the desired capabilities
chrome_caps = {
    "build": "1.0",
    "name": "Selenium Python Test",
    "platform": "Windows 10",
    "browserName":  "Chrome",
    "version":  "latest"
}

firefox_caps = {
    "build": "1.0",
    "name": "Selenium Python Test",
    "platform": "Windows 10",
    "browserName":  "firefox",
    "version":  "latest"
}

#Step Three: Connect to Selenium Test using Remote Connection

@pytest.fixture(params=["chrome", "firefox"])
def driver_initialization(request):
    desired_caps={}
    if request.param == "chrome":
        options = ChromeOptions()
        options.set_capability("LT: Options", chrome_caps)
        driver = webdriver.Remote(
            command_executor=remote_url,
            options=options)

    elif  request.param == "firefox":
            options = FirefoxOptions()
            options.set_capability("LT:Optiond", firefox_caps)
            driver = webdriver.Remote(
                command_executor=remote_url,
                options=options)

    request.cls.driver = driver
    yield
    driver.close()




