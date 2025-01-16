from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class GuardSettingsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.back_button = (AppiumBy.CLASS_NAME, 'android.widget.ImageButton')
        self.title_label = (AppiumBy.XPATH, '//android.widget.TextView[@text="Guard"]')
        self.plume_guard_label = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/aiGroupHeaderTextView')
        self.online_protection_icon = (AppiumBy.ANDROID_UIAUTOMATOR,
                                       'new UiSelector().resourceId("com.plumewifi.plume.dogfood:id/iconView").instance(0)')
        self.online_protection_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Online protection")')
        self.online_protection_description = (AppiumBy.ANDROID_UIAUTOMATOR,
                                              'new UiSelector().text("Real-time threat protection against crypto-mining, ransomware, malware & more.")')
        self.online_protection_state_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enabled").instance(0)')
        self.adblocking_icon = (AppiumBy.ANDROID_UIAUTOMATOR,
                                       'new UiSelector().resourceId("com.plumewifi.plume.dogfood:id/iconView").instance(1)')
        self.adblocking_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Adblocking")')
        self.adblocking_description = (AppiumBy.ANDROID_UIAUTOMATOR,
                                              'new UiSelector().text("Enjoy a better online experience by blocking ads")')
        self.adblocking_state_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Custom")')
        self.advanced_iot_protection_icon = (AppiumBy.ANDROID_UIAUTOMATOR,
                                       'new UiSelector().resourceId("com.plumewifi.plume.dogfood:id/iconView").instance(2)')
        self.advanced_iot_protection_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Advanced IoT protection")')
        self.advanced_iot_protection_description = (AppiumBy.ANDROID_UIAUTOMATOR,
                                              'new UiSelector().text("Protect your home network and connected devices against hackers and cybercriminals")')
        self.advanced_iot_protection_state_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enabled").instance(1)')
        self.manage_security_events_button = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/manageSecurityEventsTextView')
        self.let_me_be_label = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/letMeBe')
        self.privacy_mode_icon = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.plumewifi.plume.dogfood:id/iconView").instance(3)')
        self.privacy_mode_state_label = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/titleView')
        self.privacy_mode_toggle = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/switchWiew')
        self.delete_security_events_icon = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/view_item_icon')
        self.delete_security_events_button = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/view_item_title')
        self.learn_more_label = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/privacyModeDescription')

        self.initial_views = [
            self.back_button,
            self.title_label,
            self.plume_guard_label,
            self.online_protection_icon,
            self.online_protection_label,
            self.online_protection_description,
            self.online_protection_state_label,
            self.adblocking_icon,
            self.adblocking_label,
            self.adblocking_description,
            self.adblocking_state_label,
            self.advanced_iot_protection_icon,
            self.advanced_iot_protection_label,
            self.advanced_iot_protection_description,
            self.advanced_iot_protection_state_label,
            self.manage_security_events_button,
            self.let_me_be_label,
            self.privacy_mode_icon,
            self.privacy_mode_state_label,
            self.privacy_mode_toggle,
            self.delete_security_events_icon,
            self.delete_security_events_button,
            self.learn_more_label
        ]

    def tap_back_button(self):
        self.driver.find_element(*self.back_button).click()
        return self

    def tap_online_protection_label(self):
        self.driver.find_element(*self.online_protection_label).click()
        return self

    def tap_adblocking_label(self):
        self.driver.find_element(*self.adblocking_label).click()
        return self

    def tap_advanced_iot_protection_label(self):
        self.driver.find_element(*self.advanced_iot_protection_label).click()
        return self

    def tap_manage_security_events_button(self):
        self.driver.find_element(*self.manage_security_events_button).click()
        return self

    def tap_privacy_mode_toggle(self):
        self.driver.find_element(*self.privacy_mode_toggle).click()
        return self

    def tap_delete_security_events_button(self):
        self.driver.find_element(*self.delete_security_events_button).click()
        return self

    def tap_learn_more_label(self):
        self.driver.find_element(*self.learn_more_label).click()
        return self
