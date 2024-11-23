from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class TermsAndConditionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.web_view = (AppiumBy.ID, "webView")
        self.accept_button = (AppiumBy.ID, 'acceptButton')
        self.cancel_button = (AppiumBy.ID, 'cancelButton')

        self.initial_views = [
            self.web_view,
            self.accept_button,
            self.cancel_button
        ]

    def tap_accept_button(self):
        self.driver.find_element(*self.accept_button).click()
        return self

    def tap_cancel_button(self):
        self.driver.find_element(*self.cancel_button).click()
        return self