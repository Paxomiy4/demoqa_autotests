from ..pages.elements_pages.elements_page import ElementsPage
from ..pages.main_page import MainPage
from ..pages.forms_pages.forms_page import FormsPage
from ..pages.alerts_pages.alerts_page import AlertsPage
from ..pages.widgets_pages.widgets_page import WidgetsPage
from ..pages.interactions_pages.intersctions_page import InteractionsPage
from ..pages.book_store_pages.book_store_page import BookStorePage


LINK = "https://demoqa.com/"


def test_go_to_elements_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_elements_page()
    elements_page = ElementsPage(browser, browser.current_url)
    elements_page.should_be_elements_page()


def test_go_to_forms_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_forms_page()
    forms_page = FormsPage(browser, browser.current_url)
    forms_page.should_be_forms_page()


def test_go_to_alerts_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_alerts_page()
    alerts_page = AlertsPage(browser, browser.current_url)
    alerts_page.should_be_alerts_page()


def test_go_to_widgets_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_widgets_page()
    widgets_page = WidgetsPage(browser, browser.current_url)
    widgets_page.should_be_widgets_page()


def test_go_to_interactions_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_interactions_page()
    interactions_page = InteractionsPage(browser, browser.current_url)
    interactions_page.should_be_interactions_page()


def test_go_to_book_store_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_book_store_page()
    book_store_page = BookStorePage(browser, browser.current_url)
    book_store_page.should_be_bookstore_page()
