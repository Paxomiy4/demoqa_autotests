from ..base_page import BasePage
from ..locators import TextBoxPageLocators


class TextBoxPage(BasePage):
    def should_be_text_box_page(self):
        self.should_be_text_box_url()
        self.should_be_text_box_header()

    def should_be_text_box_url(self):
        assert "text-box" in self.browser.current_url

    def should_be_text_box_header(self):
        text_box_header = self.browser.find_element(*TextBoxPageLocators.HEADER)
        assert text_box_header.text == "Text Box", "Text Box header not present"