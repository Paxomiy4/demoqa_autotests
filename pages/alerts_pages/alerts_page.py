from ..base_page import BasePage
from ..locators import AlertsPageLocators


class AlertsPage(BasePage):
    def should_be_alerts_page(self):
        self.should_be_alerts_url()
        self.should_be_alerts_header()

    def should_be_alerts_url(self):
        assert "alertsWindows" in self.browser.current_url

    def should_be_alerts_header(self):
        alerts_header = self.browser.find_element(*AlertsPageLocators.HEADER)
        assert alerts_header.text == "Alerts, Frame & Windows", "Alerts header not present"