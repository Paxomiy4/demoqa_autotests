from ..base_page import BasePage
from ..locators import ElementsPageLocators


class ElementsPage(BasePage):
    def should_be_elements_page(self):
        self.should_be_elements_url()
        self.should_be_elements_header()

    def should_be_elements_url(self):
        assert "elements" in self.browser.current_url

    def should_be_elements_header(self):
        elements_header = self.browser.find_element(*ElementsPageLocators.HEADER)
        assert elements_header.text == "Elements", "Elements header not present"

    def go_to_text_box_page(self):
        button = self.browser.find_element(*ElementsPageLocators.TEXT_BOX)
        button.click()

    def go_to_check_box_page(self):
        button = self.browser.find_element(*ElementsPageLocators.CHECK_BOX)
        button.click()
