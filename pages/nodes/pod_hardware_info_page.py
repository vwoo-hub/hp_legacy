from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class PodHardwareInfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.firmware_version_label = (AppiumBy.ID, 'hardware_firmware_version_key_label')
        self.ethernet_mac_label = (AppiumBy.XPATH, '//android.widget.TextView[@text="Ethernet MAC"]')
        self.ethernet_2_mac_label = (AppiumBy.XPATH, '//android.widget.TextView[@text="Ethernet 2 MAC"]')
        self.serial_number_label = (AppiumBy.XPATH, '//android.widget.TextView[@text="Serial Number"]')
        self.mac_address_1_label = (AppiumBy.XPATH, '//android.widget.TextView[@text="2.4 GHz MAC"]')
        self.mac_address_2_label = (AppiumBy.XPATH, '//android.widget.TextView[@text="5 GHz MAC 1"]')
        self.mac_address_3_label = (AppiumBy.XPATH, '//android.widget.TextView[@text="5 GHz MAC 2"]')
        self.lan_ip_address_label = (AppiumBy.XPATH, '//android.widget.TextView[@text="LAN IP address"]')
        self.public_ip_address_label = (AppiumBy.ID, 'public_ip_address_label')
        self.hardware_label = (AppiumBy.XPATH, '//android.widget.TextView[@text="Hardware"]')

        self.initial_views = [
            self.firmware_version_label,
            self.ethernet_mac_label,
            self.ethernet_2_mac_label,
            self.serial_number_label,
            self.mac_address_1_label,
            self.mac_address_2_label,
            self.mac_address_3_label,
            self.lan_ip_address_label,
            self.public_ip_address_label,
            self.hardware_label
        ]
