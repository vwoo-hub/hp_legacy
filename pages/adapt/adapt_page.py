from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class AdaptPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.adapt_label = (AppiumBy.XPATH, '//android.widget.TextView[@text="Adapt"]')
        self.advanced_settings_button = (AppiumBy.ID, 'com.plumewifi.plume.dogfood:id/advanced_settings')
        self.overflow_button = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="More options"]')
        self.wifi_name_label = (AppiumBy.ID, 'wifi_edit_ssid_name_label')
        self.plume_pods_label = (AppiumBy.ID, 'pod_settings_pods_list_label')
        self.pod_one_button = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.plumewifi.plume.dogfood:id/name_TextView" and @text="ROOM 1"]')
        self.offline_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Offline").instance(0)')
        self.pod_overflow_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.plumewifi.plume.dogfood:id/overflow_ImageButton").instance(0)')
        self.set_up_new_pods_button = (AppiumBy.ID, 'pod_settings_setup_label')
        self.extend_your_wifi_coverage_label = (AppiumBy.ID, 'pod_purchase_title_label')
        self.add_a_pod_to_my_account_button = (AppiumBy.ID, 'pod_purchase_button')

        self.initial_views = [
            self.adapt_label,
            self.advanced_settings_button,
            self.overflow_button,
            self.wifi_name_label,
            self.pod_one_button,
            self.offline_label,
            self.pod_overflow_button,
            self.extend_your_wifi_coverage_label,
            self.add_a_pod_to_my_account_button
        ]

    def type_name_field(self, name):
        pass