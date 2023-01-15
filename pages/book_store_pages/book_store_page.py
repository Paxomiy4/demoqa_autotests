from ..base_page import BasePage
from ..locators import BookStorePageLocators


class BookStorePage(BasePage):
    def should_be_bookstore_page(self):
        self.should_be_bookstore_url()
        self.should_be_bookstore_header()

    def should_be_bookstore_url(self):
        assert "books" in self.browser.current_url

    def should_be_bookstore_header(self):
        bookstore_header = self.browser.find_element(*BookStorePageLocators.HEADER)
        assert bookstore_header.text == "Book Store", "Forms header not present"