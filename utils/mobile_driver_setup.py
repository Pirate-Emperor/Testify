from appium import webdriver
from selenium.common.exceptions import WebDriverException
from appium.options.android import UiAutomator2Options
from driver_setup import DriverSetup


class MobileDriverSetup(DriverSetup):
    """
    A class to manage the setup and teardown of Mobile WebDriver for Appium tests.
    """
    def __init__(self):
        super().__init__()
        self.appium_server_url = self.get_appium_server_url()
        self.desired_capabilities = self.get_mobile_desired_capabilities()

    def create_mobile_driver(self) -> webdriver.Remote:
        """
        Create a mobile WebDriver instance based on the specified desired capabilities.

        :return: A mobile WebDriver instance.
        :raises WebDriverException: If there are issues initializing the mobile WebDriver.
        :raises Exception: For any unexpected errors during driver creation.
        """
        try:
            self.logger.info('Attempting to initialize Mobile WebDriver')
            desired_capabilities = UiAutomator2Options().load_capabilities(self.desired_capabilities)
            self.driver = webdriver.Remote(self.appium_server_url, options=desired_capabilities)
            self.logger.info('Mobile driver successfully initialized')
            return self.driver
        except WebDriverException as e:
            self.logger.error(f'Mobile driver encountered an error during initialization. Error: {e}.')
            raise
        except Exception as e:
            self.logger.error(f'An unexpected error occurred while initializing the mobile driver. Error: {e}.')
            raise

    def get_mobile_desired_capabilities(self) -> dict:
        """
        Retrieve the mobile desired capabilities from the config.json file

        :return desired_capabilities: A dictionary containing the mobile desired capabilities.
        :raises Exception: If there is an unexpected error occurs during getting mobile desired capabilities.
        """
        try:
            self.logger.info('Attempting to retrieve mobile desired capabilities from the config.json')
            desired_capabilities = self.config.get_mobile_desired_capabilities()
            self.logger.info(f'Mobile desired capabilities retrieved successfully. '
                             f'Desired capabilities: {desired_capabilities}')
            return desired_capabilities
        except Exception as e:
            self.logger.error(f'An unexpected error occurred while getting mobile desired capabilities. Error: {e}')
            raise

    def get_appium_server_url(self) -> str:
        """
        Retrieve the appium server url from the config.json file.

        :return appium_server_url: the appium server url.
        :raises Exception: If there is an unexpected error occurs during getting appium server url.
        """
        try:
            self.logger.info('Attempting to retrieve Appium server url from the config.json')
            appium_server_url = self.config.get_mobile_appium_server()
            self.logger.info(f'Appium server url retrieved successfully. Appium server url: {appium_server_url}')
            return appium_server_url
        except Exception as e:
            self.logger.error(f'Unexpected error occurred while getting Appium server url. Error: {e}')
            raise
