from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class SignUpVerificationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.title_label = (AppiumBy.ID, "headerTextView")
        self.description_label = (AppiumBy.ID, 'subHeaderTextView')
        self.email_icon = (AppiumBy.ID, 'iconVerifyEmail')
        self.badge_icon = (AppiumBy.ID, 'badgePopup')
        self.resend_verification_email_button = (AppiumBy.ID, 'resendEmailButton')
        self.open_mail_app_button = (AppiumBy.ID, 'openMailButton')

        self.initial_views = [
            self.title_label,
            self.description_label,
            self.email_icon,
            self.badge_icon,
            self.resend_verification_email_button,
            self.open_mail_app_button
        ]

    def tap_resend_verification_email_button(self):
        self.driver.find_element(*self.resend_verification_email_button).click()
        return self

    def tap_open_mail_app_button(self):
        self.driver.find_element(*self.open_mail_app_button).click()
        return self