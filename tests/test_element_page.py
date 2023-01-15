from ..pages.elements_pages.elements_page import ElementsPage
from ..pages.elements_pages.text_box_page import TextBoxPage
from ..pages.elements_pages.check_box_page import CheckBoxPage

LINK = "https://demoqa.com/elements"


def test_go_to_text_box_page(browser):
    page = ElementsPage(browser, LINK)
    page.open()
    page.go_to_text_box_page()
    text_box_page = TextBoxPage(browser, browser.current_url)
    text_box_page.should_be_text_box_page()


def test_go_to_check_box_page(browser):
    page = ElementsPage(browser, LINK)
    page.open()
    page.go_to_check_box_page()
    check_box_page = CheckBoxPage(browser, browser.current_url)
    check_box_page.should_be_check_box_page()
