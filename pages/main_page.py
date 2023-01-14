from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_elements_page(self):
        button = self.browser.find_element(*MainPageLocators.ELEMENTS)
        button.click()

    def go_to_forms_page(self):
        button = self.browser.find_element(*MainPageLocators.FORMS)
        button.click()

    def go_to_alerts_page(self):
        button = self.browser.find_element(*MainPageLocators.ALERTS)
        button.click()

    def go_to_widgets_page(self):
        button = self.browser.find_element(*MainPageLocators.WIDGETS)
        button.click()

    def go_to_interactions_page(self):
        button = self.browser.find_element(*MainPageLocators.INTERACTIONS)
        button.click()

    def go_to_book_store_page(self):
        button = self.browser.find_element(*MainPageLocators.BOOK_STORE)
        button.click()
