import pytest

from pages.adapt.adapt_page import AdaptPage
from pages.home_page import HomePage
from pages.navigation_sidebar_page import NavigationSidebarPage
from pages.nodes.pod_action_sheet_page import PodActionSheetPage
from pages.nodes.pod_details_page import PodDetailsPage
from pages.nodes.pod_hardware_info_page import PodHardwareInfoPage
from tests.base_test import BaseTest


@pytest.mark.sign_in_required
class TestAdapt(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_pages(self):
        self.home_page = HomePage(self.driver)
        self.navigation_sidebar_page = NavigationSidebarPage(self.driver)
        self.adapt_page = AdaptPage(self.driver)
        self.pod_details_page = PodDetailsPage(self.driver)
        self.pod_action_sheet_page = PodActionSheetPage(self.driver)
        self.pod_hardware_info_page = PodHardwareInfoPage(self.driver)

    def test_when_navigate_to_adapt_then_verify_ui_elements(self):
        with self.home_page.wait_for_page() as page:
            page.tap_hamburger_button()

        with self.navigation_sidebar_page.wait_for_page() as page:
            page.tap_adapt_button()

        with self.adapt_page.wait_for_page():
            pass

    def test_when_tap_online_pod_then_verify_pod_details(self):
        with self.home_page.wait_for_page() as page:
            page.tap_hamburger_button()

        with self.navigation_sidebar_page.wait_for_page() as page:
            page.tap_adapt_button()

        with self.adapt_page.wait_for_page() as page:
            page.tap_pod_two_button()

        with self.pod_details_page.wait_for_page():
            pass

    def test_when_tap_online_pod_then_verify_hardware_info(self):
        with self.home_page.wait_for_page() as page:
            page.tap_hamburger_button()

        with self.navigation_sidebar_page.wait_for_page() as page:
            page.tap_adapt_button()

        with self.adapt_page.wait_for_page() as page:
            page.tap_pod_two_button()

        with self.pod_details_page.wait_for_page() as page:
            page.tap_overflow_button()

        with self.pod_action_sheet_page.wait_for_page() as page:
            page.tap_view_hardware_info_button()

        with self.pod_hardware_info_page.wait_for_page():
            pass

