from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class SpeedQualityPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.title_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("What is ISP Speed?")')
        self.subtitle_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("This is the internet speed being delivered to your home by your Internet Service Provider (ISP). For example, the pods connected to your internet Modem or Router would be receiving this speed. Here’s what the various speeds mean for quality of online experiences.")')
        self.blazing_fast_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Blazing Fast")')
        self.blazing_fast_value_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("More than 75 Mbps")')
        self.blazing_fast_description_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("The world is your oyster. Your internet supports anything you can throw at it.")')
        self.speedy_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Speedy!")')
        self.speedy_value_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("30 – 75 Mbps")')
        self.speedy_description_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4K streaming is no problem in this household.")')
        self.decent_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Decent")')
        self.decent_value_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("10 – 30 Mbps")')
        self.decent_description_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("HD streaming is no problem for you, but 4k video may struggle.")')
        self.basic_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Basic")')
        self.basic_value_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Less than 10 Mbps")')
        self.basic_description_label = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Basic services are fine, but HD streaming may be challenging.")')

        self.initial_views = [
            self.title_label,
            self.subtitle_label,
            self.blazing_fast_label,
            self.blazing_fast_value_label,
            self.blazing_fast_description_label,
            self.speedy_label,
            self.speedy_value_label,
            self.speedy_description_label,
            self.decent_label,
            self.decent_value_label,
            self.decent_description_label,
            self.basic_label,
            self.basic_value_label,
            self.basic_description_label
        ]
