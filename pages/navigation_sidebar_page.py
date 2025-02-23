from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class NavigationSidebarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.plume_logo_icon = (AppiumBy.ID, "logo_view_base_image")
        self.name_label = (AppiumBy.ID, 'name_TextView')
        self.email_label = (AppiumBy.ID, 'email_TextView')
        self.adapt_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Adapt")')
        self.access_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Access")')
        self.guard_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Guard")')
        self.sense_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sense")')
        self.support_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Support")')
        self.account_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Account")')
        self.sign_out_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sign out")')

        self.initial_views = [
            self.plume_logo_icon,
            self.name_label,
            self.email_label,
            self.adapt_button,
            self.access_button,
            self.guard_button,
            self.sense_button,
            self.support_button,
            self.account_button,
            self.sign_out_button
        ]

    def tap_adapt_button(self):
        self.wait_for_views([self.adapt_button])
        self.driver.find_element(*self.adapt_button).click()
        return self

    def tap_guard_button(self):
        self.wait_for_views([self.guard_button])
        self.driver.find_element(*self.guard_button).click()
        return self

    def tap_support_button(self):
        self.wait_for_views([self.sign_out_button])
        self.driver.find_element(*self.support_button).click()
        return self

    def tap_sign_out_button(self):
        self.wait_for_views([self.sign_out_button])
        self.driver.find_element(*self.sign_out_button).click()
        return self


