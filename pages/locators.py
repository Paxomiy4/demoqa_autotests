from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO = (By.XPATH, "//header//a")


class MainPageLocators:
    ELEMENTS = (By.XPATH, "//h5[text()='Elements']/../..")
    FORMS = (By.XPATH, "//h5[text()='Forms']/..")
    ALERTS = (By.XPATH, "//h5[text()='Alerts, Frame & Windows'/../..")
    WIDGETS = (By.XPATH, "//h5[text()='Widgets'/../..")
    INTERACTIONS = (By.XPATH, "//h5[text()='interactions'/../..")
    BOOK_STORE = (By.XPATH, "//h5[text()='Book Store Application'/../..")


class ElementsPageLocators:
    HEADER = (By.CSS_SELECTOR, ".main-header")
