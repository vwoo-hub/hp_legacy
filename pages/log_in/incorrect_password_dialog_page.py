from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class IncorrectPasswordDialogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.titleLabel = (AppiumBy.ID, "blurred_dialog_header")
        self.subtitleLabel = (AppiumBy.ID, "blurred_dialog_description")
        self.reset_button = (AppiumBy.ID, "blurred_dialog_negative_button")
        self.try_again_button = (AppiumBy.ID, "blurred_dialog_positive_button")

        self.initial_views = [
            self.titleLabel,
            self.subtitleLabel,
            self.reset_button,
            self.try_again_button
        ]

    def tap_reset_button(self):
        self.driver.find_element(*self.reset_button).click()
        return self

    def tap_try_again_button(self):
        self.driver.find_element(*self.try_again_button).click()
        return self
