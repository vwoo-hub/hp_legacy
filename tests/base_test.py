import allure
import pytest
from allure_commons.types import AttachmentType

from driver.appium_driver import AppiumDriver
from pages.home_page import HomePage
from pages.landing_page import LandingPage
from pages.sign_in.sign_in_page import SignInPage


class BaseTest(AppiumDriver):
    @pytest.fixture(autouse=True)
    def setup_driver(self, start_driver, request):
        self.driver = start_driver

        if "sign_in_required" in request.keywords:
            self.pre_sign_in()

        yield self.driver
        print("base test yield")

    def pre_sign_in(self):
        self.landing_page = LandingPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.home_page = HomePage(self.driver)

        with self.landing_page.wait_for_page() as page:
            page.tap_log_in_button()

        with self.sign_in_page.wait_for_page() as page:
            page.type_email_text_field("vwoo+hp@plume.com")
            page.type_password_text_field("plumewifi1")
            page.tap_sign_in_button()

        with self.home_page.wait_for_page():
            pass

    @pytest.fixture(autouse=True)
    def screenshot_failure(self, request):
        yield
        item = request.node
        if hasattr(item, "rep_call") and item.rep_call.failed:
            try:
                print(f"Driver state before screenshot: {self.driver}")
                if self.driver:
                    allure.attach(
                        self.driver.get_screenshot_as_png(),
                        name="screenshot_on_failure",
                        attachment_type=AttachmentType.PNG,
                    )
                else:
                    print("Driver is None; cannot capture screenshot.")
            except Exception as e:
                print(f"Screenshot failure error: {type(e).__name__}: {e}")
                raise