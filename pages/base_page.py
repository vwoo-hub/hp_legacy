from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    initial_views = []

    def __init__(self, driver):
        self.driver = driver

    def assert_initial_views(self, matchers, timeout=10):
        for matcher in matchers:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(matcher))

    def wait_for_views(self, matchers, timeout=10):
        for matcher in matchers:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(matcher))

    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
        except Exception as e:
            print(f"Keyboard not open or could not be hidden: {e}")

    def scroll_to_matcher(self, matcher):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView({matcher})')