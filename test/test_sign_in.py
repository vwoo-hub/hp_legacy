import time
import pytest

from pages.home_page import HomePage
from pages.landing_page import LandingPage
from driver.appium_driver import AppiumDriver
from pages.log_in_page import LogInPage

@pytest.mark.usefixtures("start_driver")
class TestSignIn(AppiumDriver):
    def test_when_valid_credentials_then_log_in_successfully(self):
        # initialize test pages
        landing_page = LandingPage(self.driver)
        log_in_page = LogInPage(self.driver)
        home_page = HomePage(self.driver)

        # test steps
        with landing_page.with_page_when_ready():
            landing_page.tap_log_in_button()

        with log_in_page.with_page_when_ready():
            log_in_page.type_email_text_field("vwoo+hp@plume.com")
            log_in_page.type_password_text_field("plumewifi1")
            log_in_page.tap_next_button()

        # perform assertions
        home_page.view_initial_views()

