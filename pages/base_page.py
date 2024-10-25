import logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from utils.logging_config import setup_logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
setup_logger()


class BasePage:

    def __init__(self, driver, timeout: int = 10):
        """
        Initializes the BasePage class.

        :param driver: Appium/Selenium WebDriver instance.
        :param timeout: Timeout duration for waiting for elements (default is 10 seconds).
        """
        self.driver = driver
        self.timeout = timeout
        self.logger = logging.getLogger(__name__)

    def find_element(self, locator: tuple) -> WebElement:
        """
        Find a single element with visibility condition.

        :param locator: Tuple containing (By.<method>, locator string), e.g., (By.ID, "element_id").
        :return: The mobile element is found.
        :raises TimeoutException: If the element isn't found within the timeout.
        :raises WebDriverException: If there are issues with WebDriver.
        """
        try:
            self.logger.info(f'Finding element with locator: {locator} with waiting {self.timeout} sec te be visible.')
            element = WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException as e:
            self.logger.error(f'Element not found or not visible! Locator: {locator}, Error: {str(e)}')
            raise
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to find an element! Locator:{locator}. Error: {str(e)}')
            raise

    def find_elements(self, locator: tuple) -> list[WebElement]:
        """
        Find all elements on the web page with presence condition.

        :param locator: Tuple containing (By.<method>, locator string), e.g., (By.ID, "element_id").
        :return: List of web elements found.
        :raises TimeoutException: If the elements aren't found within the timeout.
        :raises WebDriverException: If there are issues with WebDriver.
        """
        try:
            self.logger.info(f'Finding elements with locator {locator} with waiting {self.timeout} sec te be presence.')
            elements = WebDriverWait(self.driver, self.timeout).until(
                ec.presence_of_all_elements_located(locator)
            )
            return elements
        except TimeoutException as e:
            self.logger.error(f'Elements not found or not presence! Locator: {locator}, Error: {str(e)}')
            raise
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to find elements! Locator:{locator}. Error: {str(e)}')
            raise
