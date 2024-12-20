from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class SupportPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.title_label = (AppiumBy.XPATH, '//android.widget.TextView[@text="Support"]')
        self.back_button = (AppiumBy.XPATH, '//android.widget.ImageButton')
        self.get_support_label = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/customer_support_support_title')
        self.faq_button = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/faqTextView')
        self.call_us_button = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/callPlumeLinearLayout')
        self.email_us_button = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/customer_support_contact_layout')
        self.support_email_label = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/customer_support_email')
        self.about_us_label = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/customer_support_about_title')
        self.app_version_label = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/customer_support_app_version_key_label')
        self.terms_and_conditions_button = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/termsTextView')
        self.trademarks_button = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/trademarks_text')
        self.privacy_button = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/privacyTextView')

        self.initial_views = [
            self.title_label,
            self.back_button,
            self.get_support_label,
            self.faq_button,
            self.call_us_button,
            self.email_us_button,
            self.support_email_label,
            self.about_us_label,
            self.app_version_label,
            self.terms_and_conditions_button,
            self.trademarks_button,
            self.privacy_button
        ]

    def tap_back_button(self):
        self.driver.find_element(*self.back_button).click()
        return self

