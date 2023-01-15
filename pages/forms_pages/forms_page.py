from ..base_page import BasePage
from ..locators import FormsPageLocators


class FormsPage(BasePage):
    def should_be_forms_page(self):
        self.should_be_forms_url()
        self.should_be_forms_header()

    def should_be_forms_url(self):
        assert "forms" in self.browser.current_url

    def should_be_forms_header(self):
        forms_header = self.browser.find_element(*FormsPageLocators.HEADER)
        assert forms_header.text == "Forms", "Forms header not present"