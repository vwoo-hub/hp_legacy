import pytest

from pages.home_page import HomePage
from pages.landing_page import LandingPage
from pages.navigation_sidebar_page import NavigationSidebarPage
from pages.sign_in.sign_in_page import SignInPage
from pages.support.support_page import SupportPage
from tests.base_test import BaseTest


class TestAdapt(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_pages(self):
        self.landing_page = LandingPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.navigation_sidebar_page = NavigationSidebarPage(self.driver)
        self.support_page = SupportPage(self.driver)


    def test_when_navigate_to_support_then_verify_ui_elements(self):
        with self.landing_page.wait_for_page() as page:
            page.tap_log_in_button()

        with self.sign_in_page.wait_for_page() as page:
            page.type_email_text_field("vwoo+hp@plume.com")
            page.type_password_text_field("plumewifi1")
            page.tap_sign_in_button()

        with self.home_page.wait_for_page() as page:
            page.tap_hamburger_button()

        with self.navigation_sidebar_page.wait_for_page() as page:
            page.tap_support_button()

        with self.support_page.wait_for_page():
            pass


