from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class SuspiciousActivityBannerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


        self.title_label = (AppiumBy.ID, "TextView_title")
        self.description_label = (AppiumBy.ID, "TextView_description")
        self.tell_me_more_button = (AppiumBy.ID, "Button_primary")

        self.initial_views = [
            self.title_label,
            self.description_label,
            self.tell_me_more_button
        ]

    def tap_tell_me_more_button(self):
        self.driver.find_element(*self.tell_me_more_button).click()
        return self