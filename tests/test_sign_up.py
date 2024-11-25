import pytest

from pages.landing_page import LandingPage
from pages.log_in.log_in_page import LogInPage
from pages.sign_up.email_exists_dialog_page import EmailExistsDialogPage
from pages.sign_up.sign_up_page import SignUpPage
from pages.sign_up.sign_up_password_page import SignUpPasswordPage
from pages.sign_up.sign_up_verification_page import SignUpVerificationPage
from pages.sign_up.terms_and_conditions_page import TermsAndConditionsPage
from tests.base_test import BaseTest
from util.generate_email import generate_email


class TestSignUp(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_pages(self):
        self.landing_page = LandingPage(self.driver)
        self.terms_and_conditions_page = TermsAndConditionsPage(self.driver)
        self.sign_up_page = SignUpPage(self.driver)
        self.sign_up_password_page = SignUpPasswordPage(self.driver)
        self.sign_up_verification_page = SignUpVerificationPage(self.driver)
        self.email_exists_dialog_page = EmailExistsDialogPage(self.driver)
        self.log_in_page = LogInPage(self.driver)

    def test_when_valid_credentials_then_show_verify_email(self):
        with self.landing_page.wait_for_page(10) as page:
            page.tap_set_up_plume_button()

        with self.terms_and_conditions_page.wait_for_page() as page:
            page.tap_accept_button()

        with self.sign_up_page.wait_for_page() as page:
            page.type_name_field("vwoo test")
            page.type_email_field(generate_email())
            page.tap_next_button()

        with self.sign_up_password_page.wait_for_page() as page:
            page.type_password_field("password123")
            page.tap_next_button()

        with self.sign_up_verification_page.wait_for_page() as page:
            page.tap_resend_verification_email_button()

    def test_when_email_exists_then_shows_error_dialog(self):
        with self.landing_page.wait_for_page(10) as page:
            page.tap_set_up_plume_button()

        with self.terms_and_conditions_page.wait_for_page() as page:
            page.tap_accept_button()

        with self.sign_up_page.wait_for_page() as page:
            page.type_name_field("vwoo test")
            page.type_email_field("vwoo+hp@plume.com")
            page.tap_next_button()

        with self.email_exists_dialog_page.wait_for_page() as page:
            page.tap_sign_in_button()

        with self.log_in_page.wait_for_page():
            pass
