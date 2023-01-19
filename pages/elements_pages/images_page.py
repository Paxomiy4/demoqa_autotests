from ..base_page import BasePage
from ..locators import ImagesLocators


class ImagesPage(BasePage):
    def should_be_images_page(self):
        self.should_be_images_url()
        self.should_be_images_header()

    def should_be_images_url(self):
        assert "broken" in self.browser.current_url

    def should_be_images_header(self):
        images_header = self.browser.find_element(*ImagesLocators.HEADER)
        assert images_header.text == "Broken Links - Images", "Images header not present"