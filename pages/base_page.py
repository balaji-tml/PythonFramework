from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,20)

    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type(self, locator, value):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    def select_dropdown_value(self, locator, selection_type, value):
        """
        Selects an option in a dropdown menu.

        :param driver: Selenium WebDriver instance
        :param locator: Tuple or string to locate the dropdown element
        :param selection_type: 'index', 'value', or 'visible_text'
        :param value: The index (int), value (str), or text (str) to select
        """
        # Handle both tuple locators (By.ID, 'id') and string IDs/Xpaths
        if isinstance(locator, tuple):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            # element = driver.find_element(*locator)
        else:
            # Fallback for string locators; assumes ID or XPath

            element = self.wait.until(EC.visibility_of_element_located(locator))
            # element = (
            #     driver.find_element_by_id(locator)
            #     if locator.startswith("id=")
            #     else driver.find_element_by_xpath(locator)
            # )

        dropdown = Select(element)

        if selection_type == "index":
            dropdown.select_by_index(value)
        elif selection_type == "value":
            dropdown.select_by_value(value)
        elif selection_type == "visible_text":
            dropdown.select_by_visible_text(value)
        else:
            raise ValueError(
                "selection_type must be 'index', 'value', or 'visible_text'"
            )