from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.log_in_button = (AppiumBy.ID, 'splash_sign_in')
        self.set_up_plume_button = (AppiumBy.ID, 'splash_setup')

        self.initial_views = [self.log_in_button, self.set_up_plume_button]

    def tap_set_up_plume_button(self):
        self.wait_for_views([self.log_in_button])
        self.driver.find_element(*self.set_up_plume_button).click()
        return self

    def tap_log_in_button(self):
        self.wait_for_views([self.log_in_button])
        self.driver.find_element(*self.log_in_button).click()
        return self

