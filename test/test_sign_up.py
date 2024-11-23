import pytest
from pages.landing_page import LandingPage
from driver.appium_driver import AppiumDriver  # Import AppiumDriver directly
from pages.sign_up.sign_up_page import SignUpPage
from pages.sign_up.sign_up_password_page import SignUpPasswordPage
from pages.sign_up.sign_up_verification_page import SignUpVerificationPage
from pages.sign_up.terms_and_conditions_page import TermsAndConditionsPage
from util.generate_email import generate_email


@pytest.mark.usefixtures("start_driver")
class TestSignUp(AppiumDriver):  # Inherit from AppiumDriver class
    def test_when_valid_credentials_then_show_verify_email(self):
        landing_page = LandingPage(self.driver)
        terms_and_conditions_page = TermsAndConditionsPage(self.driver)
        sign_up_page = SignUpPage(self.driver)
        sign_up_password_page = SignUpPasswordPage(self.driver)
        sign_up_verification_page = SignUpVerificationPage(self.driver)

        with landing_page.wait_for_page(10) as page:
            page.tap_set_up_plume_button()

        with terms_and_conditions_page.wait_for_page() as page:
            page.tap_accept_button()

        with sign_up_page.wait_for_page() as page:
            page.type_name_field("vwoo test")
            page.type_email_field(generate_email())
            page.tap_next_button()

        with sign_up_password_page.wait_for_page() as page:
            page.type_password_field("password123")
            page.tap_next_button()

        with sign_up_verification_page.wait_for_page() as page:
            page.tap_resend_verification_email_button()
