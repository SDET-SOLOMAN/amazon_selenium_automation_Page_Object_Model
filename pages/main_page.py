from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):

    SEARCH_FIELD = (By.CSS_SELECTOR, "form#nav-search-bar-form input[type='text']")
    SEARCH_ICON = (By.CSS_SELECTOR, "div.nav-right input[class*='rogressive-att']")

    def open_main_page(self):
        self.open_page('https://www.amazon.com')

    def input_amazon_search(self, text):
        self.input_text(text, *self.SEARCH_FIELD)

    def click_on_search_icon(self):
        self.click(*self.SEARCH_ICON)