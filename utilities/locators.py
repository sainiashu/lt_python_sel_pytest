from selenium.webdriver.common.by import By

class SearchPageLocatorFields:
    search_text_field = (By.ID,"small-searchterms")
    search_button = (By.XPATH, "//input[@class='button-1 search-box-button']")