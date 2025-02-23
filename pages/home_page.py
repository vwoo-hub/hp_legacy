from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.logo_image = (AppiumBy.ID, "logo_view_base_image")
        self.partner_image = (AppiumBy.ID, "logo_view_partner_image")
        self.hamburger_button = (AppiumBy.CLASS_NAME, "android.widget.ImageButton")
        self.wifi_motion_button = (AppiumBy.ID, "menu_wifi_motion")
        self.quarantine_alert_button = (AppiumBy.ID, "Button_alertBadge")
        self.gateway_pod_icon = (AppiumBy.ID, "kingPod")
        self.network_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.plumewifi.plume.dogfood:id/imageView").instance(0)')

        self.initial_views = [
            self.logo_image,
            self.partner_image,
            self.hamburger_button,
            self.wifi_motion_button,
            self.gateway_pod_icon,
            self.network_button
        ]

    def tap_hamburger_button(self):
        self.driver.find_element(*self.hamburger_button).click()
        return self

    def tap_wifi_motion_button(self):
        self.driver.find_element(*self.wifi_motion_button).click()
        return self

    def tap_quarantine_alert_button(self):
        self.driver.find_element(*self.quarantine_alert_button).click()
        return self

    def tap_gateway_pod_icon(self):
        self.driver.find_element(*self.gateway_pod_icon).click()
        return self

    def tap_network_button(self):
        self.driver.find_element(*self.network_button).click()
        return self

