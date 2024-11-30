import pytest

from pages.home_page import HomePage
from pages.landing_page import LandingPage
from pages.log_in.log_in_page import LogInPage
from pages.log_in.reset_password_dialog_page import ResetPasswordDialogPage
from pages.log_in.reset_password_page import ResetPasswordPage
from pages.navigation_sidebar_page import NavigationSidebarPage
from tests.base_test import BaseTest


class TestHome(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_pages(self):
        self.landing_page = LandingPage(self.driver)
        self.log_in_page = LogInPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.navigation_sidebar_page = NavigationSidebarPage(self.driver)

    def test_when_on_home_screen_then_displays_navigation_sidebar(self):
        with self.landing_page.wait_for_page() as page:
            page.tap_log_in_button()

        with self.log_in_page.wait_for_page() as page:
            page.type_email_text_field("vwoo+hp@plume.com")
            page.type_password_text_field("plumewifi1")
            page.tap_sign_in_button()

        with self.home_page.wait_for_page() as page:
            page.tap_hamburger_button()

        with self.navigation_sidebar_page.wait_for_page():
            pass