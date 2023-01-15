from ..base_page import BasePage
from ..locators import WidgetsPageLocators


class WidgetsPage(BasePage):
    def should_be_widgets_page(self):
        self.should_be_widgets_url()
        self.should_be_widgets_header()

    def should_be_widgets_url(self):
        assert "widgets" in self.browser.current_url

    def should_be_widgets_header(self):
        widgets_header = self.browser.find_element(*WidgetsPageLocators.HEADER)
        assert widgets_header.text == "Widgets", "Widgets header not present"