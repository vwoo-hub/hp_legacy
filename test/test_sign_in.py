# test_sign_in.py
import time
import pytest
from pages.landing_page import LandingPage
from driver.appium_driver import AppiumDriver  # Import AppiumDriver directly
from pages.log_in_page import LogInPage


# Use the AppiumDriver fixture to start the driver
@pytest.mark.usefixtures("start_driver")
class TestSignIn(AppiumDriver):  # Inherit from AppiumDriver class
    def test_sign_in_flow(self):
        """Test the sign-in flow using LandingPage methods."""

        # Initialize the Landing Page with self.driver (inherited from AppiumDriver)
        landing_page = LandingPage(self.driver)
        log_in_page = LogInPage(self.driver)

        # Perform login steps
        landing_page.tap_log_in_button()
        log_in_page.type_email_text_field("vwoo+hp@plume.com")
        log_in_page.type_password_text_field("plumewifi1")
        log_in_page.tap_next_button()


        # Wait to observe the result, could be replaced by assertions
        time.sleep(5)

        # Placeholder for assertion (e.g., check for successful login indication)
        print("Test sign-in flow executed successfully")

# test_login.py

# import time
# import pytest
# from pages.landing_page import LandingPage
# from driver.appium_driver import start   # Import the fixture
#
# @pytest.mark.usefixtures("start")
# class TestSignIn:
#     def test_sign_in_flow(self, start):
#         # Initialize the Landing Page with the provided driver
#         landing_page = LandingPage(start)
#
#         # Perform login steps
#         landing_page.tap_sign_in_button()
#         landing_page.type_email_text_field("vwoo+hp@plume.com")
#         landing_page.tap_next_button()
#
#         # Wait to observe the result, could be replaced by assertions
#         time.sleep(5)
#
#         # Placeholder for assertion (e.g., check for successful login indication)
#         # assert appium_driver.find_element(AppiumBy.ID, "some_element_id").is_displayed()