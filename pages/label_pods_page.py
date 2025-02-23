from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class LabelPodsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.back_button = (AppiumBy.ACCESSIBILITY_ID, 'Navigate up')
        self.title_label = (AppiumBy.ID, "whichPodTitle")
        self.description_label = (AppiumBy.ID, 'whichPodDescription')
        self.label_pod_image = (AppiumBy.CLASS_NAME, 'android.widget.ImageView')
        self.label_pods_button = (AppiumBy.ID, 'Button_labelPods')

        self.initial_views = [
            self.back_button,
            self.title_label,
            self.description_label,
            self.label_pod_image,
            self.label_pods_button
        ]

    def tap_back_button(self):
        self.driver.find_element(*self.back_button).click()
        return self

    def tap_label_pods_button(self):
        self.driver.find_element(*self.label_pods_button).click()
        return self
