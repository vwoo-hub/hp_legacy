from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class PodDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.back_button = (AppiumBy.XPATH, "//android.widget.ImageButton")
        self.overflow_button = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="More options"]')
        self.pod_image = (AppiumBy.ID, 'ImageView_pod')
        self.pod_name_label = (AppiumBy.ID, 'podNameEditText')
        self.no_devices_image = (AppiumBy.ID, 'ImageView_noDevice')
        self.no_devices_label = (AppiumBy.ID, 'TextView_label')
        self.no_devices_description_label = (AppiumBy.ID, 'TextView_typical')

        self.initial_views = [
            self.back_button,
            self.overflow_button,
            self.pod_image,
            self.pod_name_label,
            self.no_devices_image,
            self.no_devices_label,
            self.no_devices_description_label
        ]

    def tap_back_button(self):
        self.driver.find_element(*self.back_button).click()
        return self

    def tap_overflow_button(self):
        self.driver.find_element(*self.overflow_button).click()
        return self
