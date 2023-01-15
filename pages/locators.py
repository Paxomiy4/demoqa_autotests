from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO = (By.XPATH, "//header//a")


class MainPageLocators:
    ELEMENTS = (By.XPATH, "//h5[text()='Elements']/../..")
    FORMS = (By.XPATH, "//h5[text()='Forms']/../..")
    ALERTS = (By.XPATH, "//h5[text()='Alerts, Frame & Windows']/../..")
    WIDGETS = (By.XPATH, "//h5[text()='Widgets']/../..")
    INTERACTIONS = (By.XPATH, "//h5[text()='Interactions']/../..")
    BOOK_STORE = (By.XPATH, "//h5[text()='Book Store Application']/../..")


class ElementsPageLocators:
    HEADER = (By.CSS_SELECTOR, ".main-header")
    TEXT_BOX = (By.XPATH, "//span[text()='Text Box']")
    CHECK_BOX = (By.XPATH, "//span[text()='Check Box']")
    RADIO_BUTTON = (By.XPATH, "//span[text()='Radio Button']")
    WEB_TABLES = (By.XPATH, "//span[text()='Web Tables']")
    BUTTONS = (By.XPATH, "//span[text()='Buttons']")
    LINKS = (By.XPATH, "//span[text()='Links']")
    IMAGES = (By.XPATH, "//span[text()='Broken Links - Images']")
    UPLOAD_AND_DOWNLOAD = (By.XPATH, "//span[text()='Upload and Download']")
    DYNAMIC_PROPERTIES = (By.XPATH, "//span[text()='Dynamic Properties']")


class TextBoxPageLocators:
    HEADER = (By.CSS_SELECTOR, ".main-header")


class CheckBoxLocators:
    HEADER = (By.CSS_SELECTOR, ".main-header")


class RadioButtonLocators:
    HEADER = (By.CSS_SELECTOR, ".main-header")


class WebTablesLocators:
    HEADER = (By.CSS_SELECTOR, ".main-header")


class ButtonsLocators:
    HEADER = (By.CSS_SELECTOR, ".main-header")


class LinksLocators:
    HEADER = (By.CSS_SELECTOR, ".main-header")


class ImagesLocators:
    HEADER = (By.CSS_SELECTOR, ".main-header")


class UploadAndDownloadLocators:
    HEADER = (By.CSS_SELECTOR, ".main-header")


class FormsPageLocators:
    HEADER = (By.CSS_SELECTOR, ".main-header")


class DynamicPropertiesLocators:
    HEADER = (By.CSS_SELECTOR, ".main-header")


class AlertsPageLocators:
    HEADER = (By.CSS_SELECTOR, ".main-header")


class WidgetsPageLocators:
    HEADER = (By.CSS_SELECTOR, ".main-header")


class InteractionsPageLocators:
    HEADER = (By.CSS_SELECTOR, ".main-header")


class BookStorePageLocators:
    HEADER = (By.CSS_SELECTOR, ".main-header")

