from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.logo_image = (AppiumBy.ID, "logo_view_base_image")
        self.partner_image = (AppiumBy.ID, "logo_view_partner_image")
        self.hamburger_button = (AppiumBy.CLASS_NAME, "android.widget.ImageButton")
        self.wifi_motion_button = (AppiumBy.ID, "menu_wifi_motion")

        self.initial_views = [
            self.logo_image,
            self.partner_image,
            self.hamburger_button,
            self.wifi_motion_button
        ]

    def tap_hamburger_button(self):
        self.wait_for_views([self.hamburger_button])
        self.driver.find_element(*self.hamburger_button).click()
        return self

    def tap_wifi_motion_button(self):
        self.wait_for_views([self.wifi_motion_button])
        self.driver.find_element(*self.wifi_motion_button).click()
        return self
