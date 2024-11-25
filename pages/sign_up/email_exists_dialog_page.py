from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class EmailExistsDialogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.title_label = (AppiumBy.ID, "blurred_dialog_header")
        self.description_label = (AppiumBy.ID, "blurred_dialog_description")
        self.try_again_button = (AppiumBy.ID, "blurred_dialog_negative_button")
        self.sign_in_button = (AppiumBy.ID, "blurred_dialog_positive_button")

        self.initial_views = [
            self.title_label,
            self.description_label,
            self.try_again_button,
            self.sign_in_button
        ]

    def tap_try_again_button(self):
        self.driver.find_element(*self.try_again_button).click()
        return self

    def tap_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()
        return self