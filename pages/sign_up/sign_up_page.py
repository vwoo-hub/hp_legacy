from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class SignUpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.title_label = (AppiumBy.ID, "headerTextView")
        self.description_label = (AppiumBy.ID, 'subHeaderTextView')
        self.profile_icon = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="com.plumewifi.plume.dogfood:id/nameLayout"]/android.widget.ImageView')
        self.name_text_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Name")')
        self.email_icon = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="com.plumewifi.plume.dogfood:id/emailLayout"]/android.widget.ImageView')
        self.email_text_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Email")')
        self.next_button = (AppiumBy.ID, 'nextButton')
        self.invalid_name_error_label = (AppiumBy.ID, 'textinput_error')

        self.initial_views = [
            self.title_label,
            self.description_label,
            self.profile_icon,
            self.name_text_field,
            self.email_icon,
            self.email_text_field,
            self.next_button
        ]

    def type_name_field(self, name):
        self.driver.find_element(*self.name_text_field).send_keys(name)
        return self

    def tap_email_field(self):
        self.driver.find_element(*self.email_text_field).click()
        return self

    def type_email_field(self, email):
        self.driver.find_element(*self.email_text_field).send_keys(email)
        return self

    def tap_next_button(self):
        self.driver.find_element(*self.next_button).click()
        return self

    def view_invalid_name_error_label(self):
        self.wait_for_views([self.invalid_name_error_label])