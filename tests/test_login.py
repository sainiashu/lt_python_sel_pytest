from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import TestData

class TestLogin(BaseTest):

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.set_email_address(TestData.username)
        login_page.set_password(TestData.password)
        login_page.click_login_button()

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login_into_application("123.Tester@test.test","password")
        actual_msg = login_page.get_warning_msg()
        assert actual_msg.__contains__("Login was unsuccessful")