from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.home_page import HomePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    email_address_field= (By.ID,"Email")
    password_field= (By.ID,"Password")
    login_btn = (By.XPATH, "//input[@value='Log in']")
    warning_msg = (By.XPATH,"//span[contains(text(),'Login was unsuccessful. Please correct the errors ')]")

    # if we do not use the super class or Basepage class we need write the complete code like this
        # "self.driver.find_element(email_address_field).send_keys(email_address)"


    def set_email_address(self,email_address):
        self.set(self.email_address_field, email_address)
        # self.driver.find_element(email_address_field).send_keys(email_address)

    def set_password(self,password):
        self.set(self.password_field,password)

    def click_login_button(self):
        self.click(self.login_btn)
        return HomePage(self.driver)

    def login_into_application(self, email, password):
        self.set_email_address(email)
        self.set_password(password)
        self.click_login_button()

    def get_warning_msg(self):
        return self.get_text(self.warning_msg)