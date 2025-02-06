from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class FaqPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.back_button = (AppiumBy.CLASS_NAME, "android.widget.ImageButton")
        self.search_text_field = (AppiumBy.CLASS_NAME, "android.widget.EditText")

        self.initial_views = [
            self.back_button,
            self.search_text_field
        ]

    def tap_back_button(self):
        self.driver.find_element(*self.back_button).click()
        return self

    def type_search_text_field(self, content):
        self.driver.find_element(*self.search_text_field).send_keys(content)
        return self
