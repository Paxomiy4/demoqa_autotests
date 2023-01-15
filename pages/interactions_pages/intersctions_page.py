from ..base_page import BasePage
from ..locators import InteractionsPageLocators


class InteractionsPage(BasePage):
    def should_be_interactions_page(self):
        self.should_be_interactions_url()
        self.should_be_interactions_header()

    def should_be_interactions_url(self):
        assert "interaction" in self.browser.current_url

    def should_be_interactions_header(self):
        interactions_header = self.browser.find_element(*InteractionsPageLocators.HEADER)
        assert interactions_header.text == "Interactions", "Interactions header not present"