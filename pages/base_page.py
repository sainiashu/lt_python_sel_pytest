from selenium.webdriver.common.by import By

class BasePage:
    """
    The purpose of the Basepage class is to contain common methods that are used in the entire All page objects
    """
    def __int__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(*locator).click()

    def set(self, locator, value):
        self.driver(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text

    def click_right_menu_page(self,page_name):
        # page = By.XPATH,"//aside[@id='column-right']//a[text()=' My Account']"
        # page = By.XPATH, "//aside[@id='column-right']//a[text()=' "+ page_name +"']"
        page = By.XPATH,"//li[@class='inactive']//a[normalize-space()='"+ page_name +"']"
        self.click(page)

# Below method allow us to click the page, Check if the page is visible and More Actions
    def page(self, page_name):
        return By.XPATH,"//li[@class='inactive']//a[normalize-space()='"+ page_name +"']"