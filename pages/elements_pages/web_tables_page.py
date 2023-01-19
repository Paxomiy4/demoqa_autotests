from ..base_page import BasePage
from ..locators import WebTablesLocators


class WebTablesPage(BasePage):
    def should_be_web_tables_page(self):
        self.should_be_web_tables_url()
        self.should_be_web_tables_header()

    def should_be_web_tables_url(self):
        assert "webtables" in self.browser.current_url

    def should_be_web_tables_header(self):
        web_tables_header = self.browser.find_element(*WebTablesLocators.HEADER)
        assert web_tables_header.text == "Web Tables", "Web Tables header not present"