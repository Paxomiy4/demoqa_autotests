from ..base_page import BasePage
from ..locators import CheckBoxLocators


class CheckBoxPage(BasePage):
    def should_be_check_box_page(self):
        self.should_be_check_box_url()
        self.should_be_check_box_header()

    def should_be_check_box_url(self):
        assert "checkbox" in self.browser.current_url

    def should_be_check_box_header(self):
        check_box_header = self.browser.find_element(*CheckBoxLocators.HEADER)
        assert check_box_header.text == "Check Box", "Check Box header not present"