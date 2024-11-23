from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.back_button = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
        self.reset_password_label = (AppiumBy.XPATH, '//android.widget.TextView[@text="Reset Password"]')
        self.email_icon = (AppiumBy.ID, "emailImageView")
        self.email_text_field = (AppiumBy.CLASS_NAME, "android.widget.EditText")
        self.reset_password_description_label = (AppiumBy.ID, "resetPasswordMessage")
        self.send_me_reset_link_button = (AppiumBy.ID, "sendResetLinkButton")

        self.initial_views = [
            self.back_button,
            self.reset_password_label,
            self.email_icon,
            self.email_text_field,
            self.reset_password_description_label,
            self.send_me_reset_link_button
        ]

    def type_email_text_field(self, email):
        self.driver.find_element(*self.email_text_field).send_keys(email)
        return self

    def tap_send_me_reset_link_button(self):
        self.driver.find_element(*self.send_me_reset_link_button).click()
        return self