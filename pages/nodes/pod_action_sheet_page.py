from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class PodActionSheetPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.edit_name_button = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.plumewifi.plume.dogfood:id/title" and @text="Edit Name"]')
        self.locate_and_name_pods_button = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.plumewifi.plume.dogfood:id/title" and @text="Locate and name pods"]')
        self.view_hardware_info_button = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.plumewifi.plume.dogfood:id/title" and @text="View Hardware Info"]')
        self.delete_pod_button = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.plumewifi.plume.dogfood:id/title" and @text="Delete Pod"]')

        self.initial_views = [
            self.edit_name_button,
            self.locate_and_name_pods_button,
            self.view_hardware_info_button,
            self.delete_pod_button
        ]

    def tap_edit_name_button(self):
        self.driver.find_element(*self.edit_name_button).click()
        return self

    def tap_locate_and_name_pods_button(self):
        self.driver.find_element(*self.locate_and_name_pods_button).click()
        return self

    def tap_view_hardware_info_button(self):
        self.driver.find_element(*self.view_hardware_info_button).click()
        return self

    def tap_delete_pod_button(self):
        self.driver.find_element(*self.delete_pod_button).click()
        return self
