from contextlib import ContextDecorator

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    initial_views = []

    def __init__(self, driver):
        self.driver = driver

    class PageReady(ContextDecorator):
        def __init__(self, base_page):
            self.base_page = base_page

        def __enter__(self):
            self.base_page.wait_for_views(self.base_page.initial_views)

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

    def with_page_when_ready(self):
        return self.PageReady(self)

    def wait_for_views(self, matchers, timeout=10, condition="visible"):
        elements = []
        for matcher in matchers:
            try:
                wait = WebDriverWait(self.driver, timeout)
                if condition == "visible":
                    element = wait.until(EC.visibility_of_element_located(matcher))
                elif condition == "clickable":
                    element = wait.until(EC.element_to_be_clickable(matcher))
                elif condition == "presence":
                    element = wait.until(EC.presence_of_element_located(matcher))
                else:
                    raise ValueError(f"Unsupported condition: {condition}")
                elements.append(element)
            except TimeoutException:
                raise TimeoutException(
                    f"Element {matcher} did not match the condition '{condition}' within {timeout} seconds.")
        return elements

    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
        except Exception as e:
            print(f"Keyboard not open or could not be hidden: {e}")

    def scroll_to_matcher(self, matcher):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView({matcher})')

