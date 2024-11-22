from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest

class AppiumDriver:
    driver = None

    @pytest.fixture()
    def start_driver(self, request):
        android_app_path = "/Users/vwoo/PycharmProjects/hp_legacy/build/legacy.apk"
        #android_app_path = "/Users/vwoo/PycharmProjects/hp_legacy/build/app.apk"

        desired_caps = {
            'deviceName': 'Android',
            'platformName': 'Android',
            'automationName': 'UIAutomator2',
            'newCommandTimeout': 100,
            'app': android_app_path
            #'autoGrantPermissions': True
        }

        # start appium driver
        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
        self.driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
        self.driver.implicitly_wait(7)

        # make driver available to tests
        request.cls.driver = self.driver

        yield self.driver

        # teardown
        self.stop_driver()

    def stop_driver(self):
        if self.driver:
            self.driver.quit()
