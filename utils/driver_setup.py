import logging
from logging_config import setup_logger
from config_parser import ConfigParser
from selenium.common.exceptions import WebDriverException


setup_logger()


class DriverSetup:

    def __init__(self):
        self.driver = None
        self.config = ConfigParser()
        self.logger = logging.getLogger(__name__)

    def quit_driver(self) -> None:
        """
        Quit the WebDriver instance.

        :return: None.
        :raises WebDriverException: If WebDriver encountered an unexpected error during quitting.
        """
        if self.driver is not None:
            try:
                self.logger.info('Quitting the WebDriver instance')
                self.driver.quit()
                self.logger.info('The Mobile WebDriver instance is quited successfully.')
            except WebDriverException as e:
                self.logger.error(f'Failed to quit the WebDriver instance. Error: {e}.')
                raise
            finally:
                self.driver = None
