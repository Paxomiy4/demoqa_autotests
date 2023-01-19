from ..base_page import BasePage
from ..locators import LinksLocators


class LinksPage(BasePage):
    def should_be_links_page(self):
        self.should_be_links_url()
        self.should_be_links_header()

    def should_be_links_url(self):
        assert "links" in self.browser.current_url

    def should_be_links_header(self):
        links_header = self.browser.find_element(*LinksLocators.HEADER)
        assert links_header.text == "Links", "Links header not present"