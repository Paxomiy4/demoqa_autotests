from ..pages.elements_pages.elements_page import ElementsPage
from ..pages.main_page import MainPage
import time
LINK = "https://demoqa.com/"


def test_go_to_elements_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_elements_page()
    elements_page = ElementsPage(browser, browser.current_url)
    elements_page.should_be_elements_page()
