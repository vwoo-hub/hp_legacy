import pytest

from pages.guard.guard_settings_page import GuardSettingsPage
from pages.home_page import HomePage
from pages.navigation_sidebar_page import NavigationSidebarPage
from tests.base_test import BaseTest


@pytest.mark.sign_in_required
class TestGuardSettings(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_pages(self):
        self.home_page = HomePage(self.driver)
        self.navigation_sidebar_page = NavigationSidebarPage(self.driver)
        self.guard_settings_page = GuardSettingsPage(self.driver)

    def test_when_navigate_to_guard_then_verify_ui_elements(self):
        with self.home_page.wait_for_page() as page:
            page.tap_hamburger_button()

        with self.navigation_sidebar_page.wait_for_page() as page:
            page.tap_guard_button()

        with self.guard_settings_page.wait_for_page():
            pass


