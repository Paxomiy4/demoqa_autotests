from ..base_page import BasePage
from ..locators import ButtonsLocators


class ButtonsPage(BasePage):
    def should_be_buttons_page(self):
        self.should_be_buttons_url()
        self.should_be_buttons_header()

    def should_be_buttons_url(self):
        assert "buttons" in self.browser.current_url

    def should_be_buttons_header(self):
        buttons_header = self.browser.find_element(*ButtonsLocators.HEADER)
        assert buttons_header.text == "Buttons", "Buttons header not present"