from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LogInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # matchers
        self.email_text_field = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Email\")")
        self.password_text_field = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Password\")")
        self.next_button = (AppiumBy.ID, 'next_button')

        self.initial_views = [
            self.email_text_field,
            self.password_text_field,
            self.next_button
        ]

    # actions
    def type_email_text_field(self, email):
        self.wait_for_views([self.email_text_field])
        self.driver.find_element(*self.email_text_field).send_keys(email)
        self.hide_keyboard()

    def type_password_text_field(self, password):
        self.wait_for_views([self.password_text_field])
        self.driver.find_element(*self.password_text_field).send_keys(password)

    def tap_next_button(self):
        self.wait_for_views([self.next_button])
        self.driver.find_element(*self.next_button).click()


