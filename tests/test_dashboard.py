import pytest

from pages.dashboard_page import DashboardPage
from pages.home_page import HomePage
from tests.base_test import BaseTest


@pytest.mark.sign_in_required
class TestDashboard(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_pages(self):
        self.home_page = HomePage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)

    def test_when_tap_on_gateway_pod_then_navigates_to_dashboard(self):
        with self.home_page.wait_for_page() as page:
            page.tap_gateway_pod_icon()

        with self.dashboard_page.wait_for_page():
            pass


