from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    INPUT_FORM = (
        By.LINK_TEXT,
        "Input Form Submit"
    )

    def open_input_form(self):
        self.click(self.INPUT_FORM)

