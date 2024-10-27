import pytest
import logging
from selenium.webdriver.remote.webdriver import WebDriver
from utils.web_driver_setup import WebDriverSetup
from utils.mobile_driver_setup import MobileDriverSetup
from utils.logging_config import setup_logger

setup_logger()
logger = logging.getLogger(__name__)


def _teardown(driver_obj) -> None:
    """
    Tear down the WebDriver instance.

    :return: None.
    :raises Exception: When an error occurs while tearing down the web driver.
    """
    try:
        logger.info('Tearing down WebDriver after the session.')
        driver_obj.quit_driver()
        logger.info('WebDriver has been properly quit successfully.')
    except Exception as e:
        logger.error(f'An error occurred during WebDriver teardown stage. Error: {e}.')
        raise


@pytest.fixture(scope='session')
def setup_teardown_webdriver() -> WebDriver:
    """
     Fixture to manage the setup and teardown of a WebDriver instance.

    :return: A WebDriver instance.
    :raises Exception: If an error occurs during the creation of the WebDriver or its teardown.
    """
    logger.info('Setting up WebDriver for the session.')
    web_driver_setup_obj = WebDriverSetup()
    try:
        web_driver = web_driver_setup_obj.create_driver()
        logger.info('WebDriver successfully created and ready for testing.')
        yield web_driver
        _teardown(web_driver_setup_obj)
    except Exception as e:
        logger.error(f'An error occurred during WebDriver setup stage. Error: {e}.')
        raise
    finally:
        _teardown(web_driver_setup_obj)


@pytest.fixture(scope='session')
def setup_teardown_mobile_webdriver() -> WebDriver:
    """
     Fixture to manage the setup and teardown of a Mobile WebDriver instance.

    :return: A Mobile WebDriver instance.
    :raises Exception: If an error occurs during the creation of the Mobile WebDriver or its teardown.
    """
    logger.info('Setting up Mobile WebDriver for the session.')
    mobile_web_driver_setup_obj = MobileDriverSetup()
    try:
        mobile_driver = mobile_web_driver_setup_obj.create_mobile_driver()
        logger.info('Mobile WebDriver successfully created and ready for testing.')
        yield mobile_driver
    except Exception as e:
        logger.error(f'An error occurred during WebDriver setup stage. Error: {e}.')
        raise
    finally:
        _teardown(mobile_web_driver_setup_obj)
