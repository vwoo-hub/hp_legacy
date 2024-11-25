import pytest

from pages.home_page import HomePage
from pages.landing_page import LandingPage
from pages.log_in.log_in_page import LogInPage
from pages.log_in.reset_password_dialog_page import ResetPasswordDialogPage
from pages.log_in.reset_password_page import ResetPasswordPage
from tests.base_test import BaseTest


class TestSignIn(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_pages(self):
        self.landing_page = LandingPage(self.driver)
        self.log_in_page = LogInPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.reset_password_page = ResetPasswordPage(self.driver)
        self.reset_password_dialog_page = ResetPasswordDialogPage(self.driver)

    def test_when_valid_credentials_then_log_in_successfully(self):
        with self.landing_page.wait_for_page() as page:
            page.tap_log_in_button()

        with self.log_in_page.wait_for_page() as page:
            page.type_email_text_field("vwoo+hp@plume.com")
            page.type_password_text_field("plumewifi1")
            page.tap_sign_in_button()

        with self.home_page.wait_for_page():
            pass

    def test_when_valid_email_then_reset_password_successful(self):
        with self.landing_page.wait_for_page(10) as page:
            page.tap_log_in_button()

        with self.log_in_page.wait_for_page() as page:
            page.tap_forgot_password_button()

        with self.reset_password_page.wait_for_page() as page:
            page.type_email_text_field("vwoo+hp@plume.com")
            page.tap_send_me_reset_link_button()

        with self.reset_password_dialog_page.wait_for_page() as page:
            page.tap_ok_button()

        with self.reset_password_page.wait_for_page():
            pass