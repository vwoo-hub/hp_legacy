from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class TopologyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.back_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageButton").instance(0)')
        self.overflow_button = (AppiumBy.ACCESSIBILITY_ID, "More options")
        self.gateway_pod_icon = (AppiumBy.XPATH, '//android.widget.TextView[@text="ROOM 2"]')
        self.leaf_pod_1_icon = (AppiumBy.XPATH, '//android.widget.TextView[@text="ROOM 6"]')
        self.leaf_pod_2_icon = (AppiumBy.XPATH, '//android.widget.TextView[@text="ROOM 1"]')
        self.network_layer_button = (AppiumBy.ID, "fab")
        self.find_and_name_all_pods_button = (AppiumBy.ID, 'title')

        self.initial_views = [
            self.back_button,
            self.overflow_button,
            self.gateway_pod_icon,
            self.leaf_pod_1_icon,
            self.leaf_pod_2_icon,
            self.network_layer_button
        ]

    def tap_back_button(self):
        self.driver.find_element(*self.back_button).click()
        return self

    def tap_overflow_button(self):
        self.driver.find_element(*self.overflow_button).click()
        return self

    def tap_find_and_name_all_pods_button(self):
        self.driver.find_element(*self.find_and_name_all_pods_button).click()
        return self

    def tap_gateway_pod_icon(self):
        self.driver.find_element(*self.gateway_pod_icon).click()
        return self

    def tap_leaf_pod_1_icon(self):
        self.driver.find_element(*self.leaf_pod_1_icon).click()
        return self

    def tap_leaf_pod_2_icon(self):
        self.driver.find_element(*self.leaf_pod_2_icon).click()
        return self

    def network_layer_button(self):
        self.driver.find_element(*self.network_layer_button).click()
        return self
