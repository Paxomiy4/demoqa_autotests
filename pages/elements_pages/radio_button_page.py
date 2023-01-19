from ..base_page import BasePage
from ..locators import RadioButtonLocators


class RadioButtonPage(BasePage):
    def should_be_radio_button_page(self):
        self.should_be_radio_button_url()
        self.should_be_radio_button_header()

    def should_be_radio_button_url(self):
        assert "radio-button" in self.browser.current_url

    def should_be_radio_button_header(self):
        radio_button_header = self.browser.find_element(*RadioButtonLocators.HEADER)
        assert radio_button_header.text == "Radio Button", "Radio Button header not present"