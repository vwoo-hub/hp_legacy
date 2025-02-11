import pytest

from pages.home_page import HomePage
from pages.navigation_sidebar_page import NavigationSidebarPage
from pages.support.faq_page import FaqPage
from pages.support.support_page import SupportPage
from tests.base_test import BaseTest


@pytest.mark.sign_in_required
class TestAdapt(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_pages(self):
        self.home_page = HomePage(self.driver)
        self.navigation_sidebar_page = NavigationSidebarPage(self.driver)
        self.support_page = SupportPage(self.driver)
        self.faq_page = FaqPage(self.driver)

    def test_when_navigate_to_support_then_verify_ui_elements(self):
        with self.home_page.wait_for_page() as page:
            page.tap_hamburger_button()

        with self.navigation_sidebar_page.wait_for_page() as page:
            page.tap_support_button()

        with self.support_page.wait_for_page():
            pass

    def test_when_navigate_to_faq_then_display_faq_webview(self):
        with self.home_page.wait_for_page() as page:
            page.tap_hamburger_button()

        with self.navigation_sidebar_page.wait_for_page() as page:
            page.tap_support_button()

        with self.support_page.wait_for_page() as page:
            page.tap_faq_button()

        with self.faq_page.wait_for_page() as page:
            page.type_search_text_field("test search query")
            page.tap_back_button()

        with self.support_page.wait_for_page():
            pass


