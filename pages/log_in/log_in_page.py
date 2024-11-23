from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LogInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # matchers
        self.email_text_field = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Email\")")
        self.password_text_field = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Password\")")
        self.forgot_password_button = (AppiumBy.ID, "forgot_password_textView")
        self.next_button = (AppiumBy.ID, 'next_button')

        self.initial_views = [
            self.email_text_field,
            self.password_text_field,
            self.forgot_password_button,
            self.next_button
        ]

    # actions
    def type_email_text_field(self, email):
        self.driver.find_element(*self.email_text_field).send_keys(email)
        self.hide_keyboard()
        return self

    def type_password_text_field(self, password):
        self.driver.find_element(*self.password_text_field).send_keys(password)
        return self

    def tap_forgot_password_button(self):
        self.driver.find_element(*self.forgot_password_button).click()
        return self

    def tap_next_button(self):
        self.driver.find_element(*self.next_button).click()
        return self

