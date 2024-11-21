# test_sign_in.py
import time
import pytest
from pages.landing_page import LandingPage
from driver.appium_driver import AppiumDriver  # Import AppiumDriver directly


# Use the AppiumDriver fixture to start the driver
@pytest.mark.usefixtures("start_driver")
class TestSignUp(AppiumDriver):  # Inherit from AppiumDriver class
    def test_sign_in_flow(self):
        """Test the sign-in flow using LandingPage methods."""

        # Initialize the Landing Page with self.driver (inherited from AppiumDriver)
        landing_page = LandingPage(self.driver)


        # Perform login steps



        # Wait to observe the result, could be replaced by assertions


        # Placeholder for assertion (e.g., check for successful login indication)
        print("Test sign-in flow executed successfully")


