from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class SignUpPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.title_label = (AppiumBy.ID, "headerTextView")
        self.description_label = (AppiumBy.ID, 'subHeaderTextView')
        self.password_icon = (AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.plumewifi.plume.dogfood:id/pwd_edit_key_icon"]')
        self.password_text_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Password")')
        self.show_hide_button = (AppiumBy.ID, 'text_input_end_icon')
        self.password_strength_label = (AppiumBy.ID, "com.plumewifi.plume.dogfood:id/pwd_edit_stength_indicator")
        self.next_button = (AppiumBy.ID, 'nextButton')

        self.initial_views = [
            self.title_label,
            self.description_label,
            self.password_icon,
            self.password_text_field,
            self.show_hide_button,
            self.password_strength_label,
            self.next_button
        ]

    def type_password_field(self, password):
        self.driver.find_element(*self.password_text_field).send_keys(password)
        return self

    def tap_show_hide_button(self):
        self.driver.find_element(*self.show_hide_button).click()
        return self

    def tap_next_button(self):
        self.driver.find_element(*self.next_button).click()
        return self