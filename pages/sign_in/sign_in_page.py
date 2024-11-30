from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class SignInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # matchers
        self.email_text_field = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Email\")")
        self.password_text_field = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Password\")")
        self.forgot_password_button = (AppiumBy.ID, "forgot_password_textView")
        self.sign_in_button = (AppiumBy.ID, 'next_button')
        self.email_does_not_exist_error_label = (AppiumBy.ID, 'textinput_error')


        self.initial_views = [
            self.password_text_field,
            self.forgot_password_button,
            self.sign_in_button
        ]

    # actions
    def tap_email_text_field(self):
        self.driver.find_element(*self.email_text_field).click()
        return self

    def tap_custom_email_text_field(self, email):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f"new UiSelector().text(\"{email}\")").click()
        return self

    def type_email_text_field(self, email):
        self.driver.find_element(*self.email_text_field).send_keys(email)
        self.hide_keyboard()
        return self

    def tap_password_text_field(self):
        self.driver.find_element(*self.password_text_field).click()
        return self

    def type_password_text_field(self, password):
        self.driver.find_element(*self.password_text_field).send_keys(password)
        return self

    def tap_forgot_password_button(self):
        self.driver.find_element(*self.forgot_password_button).click()
        return self

    def tap_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()
        return self

    def view_email_does_not_exist_error_label(self):
        self.wait_for_views([self.email_does_not_exist_error_label])
