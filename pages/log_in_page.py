from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LogInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Define elements with locators
        self.email_text_field = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Email\")")
        self.password_text_field = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Password\")")
        self.next_button = (AppiumBy.ID, 'next_button')

    # Actions on the page
    def type_email_text_field(self, email):
        self.driver.find_element(*self.email_text_field).send_keys(email)
        self.hide_keyboard()

    def type_password_text_field(self, password):
        self.driver.find_element(*self.password_text_field).send_keys(password)

    def tap_next_button(self):
        self.driver.find_element(*self.next_button).click()


