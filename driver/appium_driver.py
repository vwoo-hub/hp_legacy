import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


class AppiumDriver:
    driver = None

    @pytest.fixture()
    def start_driver(self, request):
        android_app_path = "/Users/vwoo/PycharmProjects/hp_legacy/build/legacy.apk"
        # android_app_path = "/Users/vwoo/PycharmProjects/hp_legacy/build/app.apk"

        desired_caps = {
            'deviceName': 'Android',
            'platformName': 'Android',
            'automationName': 'UIAutomator2',
            'newCommandTimeout': 300,
            'app': android_app_path
            # 'autoGrantPermissions': True
        }

        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
        self.driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
        self.driver.implicitly_wait(7)

        request.cls.driver = self.driver
        print("Driver initialized")

        yield self.driver

        self.stop_driver()
        print("Driver teardown called")

    def stop_driver(self):
        if self.driver:
            try:
                print("Quitting driver...")
                self.driver.quit()
            except Exception as e:
                print(f"Driver quit failed: {e}")
        else:
            print("Driver already None or terminated.")

