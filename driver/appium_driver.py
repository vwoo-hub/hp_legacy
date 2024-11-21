# appium_driver.py
from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest

class AppiumDriver:
    driver = None

    # This method will initialize and return the Appium driver
    @pytest.fixture()
    def start_driver(self, request):
        """Start the Appium driver before the test class."""
        android_app_path = "/Users/vwoo/PycharmProjects/Plume/build/legacy.apk"  # Define the app path
        #android_app_path = "/Users/vwoo/PycharmProjects/Plume/build/app.apk"  # Define the app path

        # Define desired capabilities
        desired_caps = {
            'deviceName': 'Android',
            'platformName': 'Android',
            'automationName': 'UIAutomator2',
            'newCommandTimeout': 100,
            'app': android_app_path
            #'autoGrantPermissions': True
        }

        # Set up the capabilities and start the driver
        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
        self.driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
        self.driver.implicitly_wait(7)

        # Provide the driver to the tests
        request.cls.driver = self.driver  # Make driver available to tests

        yield self.driver  # Yield driver to the test

        # Teardown after the test
        self.stop_driver()

    def stop_driver(self):
        """Stop the Appium driver after the test."""
        if self.driver:
            self.driver.quit()

# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# import pytest
#
#
# class AppiumDriver:
#     def __init__(self, android_app_path):
#         self.android_app_path = android_app_path
#         self.driver = None
#
#     #@pytest.fixture(scope="module")
#     def start_driver(self):
#         # Define desired capabilities
#         desired_caps = {
#             'deviceName': 'Android',
#             'platformName': 'Android',
#             'automationName': 'UIAutomator2',
#             'newCommandTimeout': 100,
#             'app': self.android_app_path,
#             'autoGrantPermissions': True
#         }
#
#         # Set up capabilities and start driver
#         capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
#         self.driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
#         self.driver.implicitly_wait(5)
#         return self.driver
#
#     def stop_driver(self):
#         if self.driver:
#             self.driver.quit()
#
#
# # Pytest fixture to initialize and yield the driver instance
# @pytest.fixture(scope="module")
# def start():
#     android_app_path = "/Users/vwoo/PycharmProjects/Plume/build/app.apk"
#     driver_instance = AppiumDriver(android_app_path)
#
#     # Start driver and yield it for test usage
#     driver = driver_instance.start_driver()
#     yield driver
#
#     # Teardown after the test
#     driver_instance.stop_driver()
