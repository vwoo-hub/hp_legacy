import pytest

from pages.home_page import HomePage
from pages.landing_page import LandingPage
from driver.appium_driver import AppiumDriver
from pages.log_in.log_in_page import LogInPage
from pages.log_in.reset_password_dialog_page import ResetPasswordDialogPage
from pages.log_in.reset_password_page import ResetPasswordPage

@pytest.mark.usefixtures("start_driver")
class TestSignIn(AppiumDriver):
    def test_when_valid_credentials_then_log_in_successfully(self):
        landing_page = LandingPage(self.driver)
        log_in_page = LogInPage(self.driver)
        home_page = HomePage(self.driver)

        with landing_page.wait_for_page() as page:
            page.tap_log_in_button()

        with log_in_page.wait_for_page() as page:
            page.type_email_text_field("vwoo+hp@plume.com")
            page.type_password_text_field("plumewifi1")
            page.tap_next_button()

        # # perform assertions
        with home_page.wait_for_page():
            pass

    def test_when_valid_email_then_reset_password_successful(self):
        landing_page = LandingPage(self.driver)
        log_in_page = LogInPage(self.driver)
        reset_password_page = ResetPasswordPage(self.driver)
        reset_password_dialog_page = ResetPasswordDialogPage(self.driver)

        with landing_page.wait_for_page(10) as page:
            page.tap_log_in_button()

        with log_in_page.wait_for_page() as page:
            page.tap_forgot_password_button()

        with reset_password_page.wait_for_page() as page:
            page.type_email_text_field("vwoo+hp@plume.com")
            page.tap_send_me_reset_link_button()

        with reset_password_dialog_page.wait_for_page() as page:
            page.tap_ok_button()

        with reset_password_page.wait_for_page():
            pass