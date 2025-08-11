from pages.base_page import BasePage
from utilities.locators import SearchPageLocatorFields


class SearchPage(BasePage):
    def __int__(self):
        super().__int__(self.driver)
        self.locate = SearchPageLocatorFields

    def search_item(self, search_text):
        self.set(self.locate.search_text_field,search_text )
        self.click(self.locate.search_button)