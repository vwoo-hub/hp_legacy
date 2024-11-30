from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class ResetPasswordDialogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.reset_password_label = (AppiumBy.ID, "blurred_dialog_header")
        self.reset_password_description_label = (AppiumBy.ID, "blurred_dialog_description")
        self.open_mail_app_button = (AppiumBy.ID, "blurred_dialog_negative_button")
        self.ok_button = (AppiumBy.ID, "blurred_dialog_positive_button")

        self.initial_views = [
            self.reset_password_label,
            self.reset_password_description_label,
            self.open_mail_app_button,
            self.ok_button
        ]

    def tap_open_mail_app_button(self):
        self.driver.find_element(*self.open_mail_app_button).click()
        return self

    def tap_ok_button(self):
        self.driver.find_element(*self.ok_button).click()
        return self