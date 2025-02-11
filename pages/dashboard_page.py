from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.back_button = (AppiumBy.CLASS_NAME, "android.widget.ImageButton")
        self.title_label = (AppiumBy.ID, 'TextView_greeting')
        self.subtitle_label = (AppiumBy.ID, 'TextView_speedLevel')
        self.last_24h_tab = (AppiumBy.ACCESSIBILITY_ID, 'Last 24 hrs')
        self.last_7d_tab = (AppiumBy.ACCESSIBILITY_ID, 'Last 7 days')
        self.last_30d_tab = (AppiumBy.ACCESSIBILITY_ID, 'Last 30 days')
        self.download_tab = (AppiumBy.ID, 'Button_download')
        self.upload_tab = (AppiumBy.ID, 'Button_upload')
        self.most_recent_label = (AppiumBy.ID, 'TextView_mostRecentTest')
        self.auto_run_title_label = (AppiumBy.ID, 'TextView_mostRecentTest')
        self.auto_run_description_label = (AppiumBy.ID, 'TextView_mostRecentTest')
        self.auto_run_toggle = (AppiumBy.ID, 'TextView_mostRecentTest')
        self.check_speed_now_button = (AppiumBy.ID, 'TextView_buttonText')
        self.time_out_label = (AppiumBy.ID, 'home_freeze_title_label')
        self.time_out_description_label = (AppiumBy.ID, 'home_freeze_first_time_experience_description_label')
        self.time_out_edit_icon = (AppiumBy.ID, 'home_freeze_edit_button')
        self.total_data_downloaded_label = (AppiumBy.ID, 'TextView_totalDataConsumed')
        self.total_data_downloaded_value_label = (AppiumBy.ID, 'TextView_totalDataValue')
        self.most_active_devices_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Most Active Devices")')
        self.no_active_devices_icon = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)')
        self.no_activity_description1_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("There has been no activity on your")')
        self.no_activity_description2_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("WiFi network in this time period.")')

        self.initial_views = [
            self.back_button,
            self.title_label,
            self.subtitle_label,
            self.last_24h_tab,
            self.last_7d_tab,
            self.last_30d_tab,
            self.download_tab,
            self.upload_tab,
            self.most_recent_label,
            self.auto_run_title_label,
            self.auto_run_description_label,
            self.auto_run_toggle,
            self.check_speed_now_button
        ]

    def tap_back_button(self):
        self.driver.find_element(*self.back_button).click()
        return self
