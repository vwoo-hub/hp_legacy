from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class SuspiciousActivityPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.title_label = (AppiumBy.ID, "warningTitleTextView")

        self.initial_views = [
            self.title_label
        ]
