from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.common.exceptions import SessionNotCreatedException, WebDriverException
from driver_setup import DriverSetup


class WebDriverSetup(DriverSetup):
    """
    A class to manage the setup and teardown of Web WebDriver instances based on a specified browser.
    """

    def __init__(self):
        super().__init__()
        self.browser = self.get_specified_browser()

    def get_specified_browser(self) -> str:
        """
        Retrieve the specified browser from the config.json.

        :return browser: The browser name (e.g., 'chrome', 'firefox', 'edge').
        :raises ValueError: If the specified browser is not supported or specified.
        """
        try:
            self.logger.info('Getting specified browser from the config.json')
            browser = self.config.get_web_browser().lower()
            if browser not in ['chrome', 'firefox', 'edge']:
                self.logger.error('Specified browser is not supported.')
                raise ValueError(f'Specified browser {browser} is not supported.')
            return browser
        except Exception as e:
            self.logger.error(f'An error occurred while trying to retrieve the specified browser. Error: {e}')
            raise

    def create_driver(self) -> WebDriver:
        """
        Create and initialize a WebDriver instance based on the specified browser.

        :return: A WebDriver instance for the specified browser.
        :raises Exception: For any unexpected errors during driver initialization.
        """
        try:
            self.logger.info(f'Attempting to initialize Web WebDriver for browser: {self.browser}')
            self._initialize_driver()
            self.logger.info(f'{self.browser.capitalize()} Web WebDriver successfully initialized')
            return self.driver
        except Exception as e:
            self.logger.error(f'An unexpected error occurred while creating the Web WebDriver. Error: {e}')
            raise

    def _initialize_driver(self) -> None:
        """
        Initialize WebDriver based on browser type.

        :return: None.
        :raises ValueError: If the specified browser is not supported.
        :raises SessionNotCreatedException: If there is an issue with creating a session.
        :raises WebDriverException: if WebDriver encountered an unexpected error during initialization.
        """
        try:
            if self.browser == 'chrome':
                self.logger.info('Initializing Chrome WebDriver')
                self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            elif self.browser == 'edge':
                self.logger.info('Initializing Edge WebDriver')
                self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
            elif self.browser == 'firefox':
                self.logger.info('Initializing Firefox WebDriver')
                self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            else:
                self.logger.error(f'Unsupported browser: {self.browser}')
                raise ValueError(f'Unsupported browser: {self.browser}')
        except SessionNotCreatedException as e:
            self.logger.error(f'Session could not be created. Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during the initialization process. Error: {e}')
            raise
