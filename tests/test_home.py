import pytest

from pages.home_page import HomePage
from pages.navigation_sidebar_page import NavigationSidebarPage
from pages.suspicious_activity_banner_page import SuspiciousActivityBannerPage
from pages.suspicious_activity_page import SuspiciousActivityPage
from tests.base_test import BaseTest


@pytest.mark.sign_in_required
class TestHome(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_pages(self):
        self.home_page = HomePage(self.driver)
        self.navigation_sidebar_page = NavigationSidebarPage(self.driver)
        self.suspicious_activity_banner_page = SuspiciousActivityBannerPage(self.driver)
        self.suspicious_activity_page = SuspiciousActivityPage(self.driver)

    def test_when_on_home_screen_then_displays_navigation_sidebar(self):
        with self.home_page.wait_for_page() as page:
            page.tap_hamburger_button()

        with self.navigation_sidebar_page.wait_for_page():
            pass

    def test_when_tap_on_home_alert_then_shows_quarantine_alert_banner(self):
        with self.home_page.wait_for_page() as page:
            page.tap_quarantine_alert_button()

        with self.suspicious_activity_banner_page.wait_for_page() as page:
            page.tap_tell_me_more_button()

        with self.suspicious_activity_page.wait_for_page():
            pass
