from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultPage(Page):

    SEARCH_RESULT = (By.XPATH, "//div[@class='sg-col-inner']//span[contains(@class, 'tate a-text-bold')]")

    def verify_search_result(self, result_word):
        self.verify_text(result_word, *self.SEARCH_RESULT)