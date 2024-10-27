from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (TimeoutException, WebDriverException, NoSuchElementException,
                                        ElementNotInteractableException, InvalidElementStateException,
                                        StaleElementReferenceException, MoveTargetOutOfBoundsException)
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class BaseWebPage(BasePage):

    def __init__(self, driver: webdriver.Remote, timeout: int = 10):
        super().__init__(driver, timeout)

    def open_url(self, url: str) -> None:
        """
        Open the specified URL.

        :param url: URL to open.
        :return: None.
        :raises WebDriverException: WebDriver encountered an error during opening a URL.
        """
        try:
            self.logger.info(f'Opening URL: {url}')
            self.driver.get(url)
            self.logger.info(f'Page opened: {url}')
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during opening this URL:{url}. Error: {e}')
            raise

    def send_keys(self, locator: tuple, keys: str) -> None:
        """
        Send keystrokes to a web element with visible condition.

        :param locator: Tuple containing (By.<method>, locator string), e.g., (By.ID, "element_id").
        :param keys: The string of keys to send.
        :return: None.
        :raises TimeoutException: If the element isn't visible within the timeout.
        :raises WebDriverException: WebDriver encountered an error during sending keystrokes to a web element.
        """
        try:
            self.logger.info(f'Sending this keys {keys} for this element {locator} with waiting {self.timeout} '
                             f'sec to be visible.')
            element = WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(locator)
            )
            element.send_keys(keys)
        except TimeoutException as e:
            self.logger.error(f'Element isn\'t found or not visible! Locator: {locator}, Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during sending keys to an element. Error: {e}')
            raise

    def get_current_url(self) -> str:
        """
        Gets the current URL of the browser.

        :return: The current URL as a string.
        :raises WebDriverException: WebDriver encountered an error during getting the current URL.
        """
        try:
            self.logger.info('Getting current URL.')
            url = self.driver.current_url
            self.logger.info(f'Current URL: {url}')
            return url
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during getting the current URL. Error: {e}')
            raise

    def get_title(self) -> str:
        """
        Get the title of the current page.

        :return: The page title as a string.
        :raises WebDriverException: WebDriver encountered an error during getting the title of the current page.
        """
        try:
            self.logger.info('Getting title.')
            title = self.driver.title
            self.logger.info(f'Title: {title}')
            return title
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during getting the title of the current page. '
                              f'Error: {e}')
            raise

    def switch_to_frame(self, frame_reference) -> None:
        """
        Switch to a specific iframe on the page.

        :param frame_reference: The frame element, index, or name to switch to.
        :return: None.
        :raises TimeoutException: If the frame is not available within the timeout.
        :raises WebDriverException: WebDriver encountered an error during switching to a frame.
        """
        try:
            self.logger.info(f'Waiting {self.timeout} sec to be available to switch to frame: {frame_reference}.')
            WebDriverWait(self.driver, self.timeout).until(
                ec.frame_to_be_available_and_switch_to_it(frame_reference)
            )
        except TimeoutException as e:
            self.logger.error(f'Frame isn\'t available! Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during switching to a frame. Error: {e}')
            raise

    def perform_click_and_hold_action_chain(self, source_element: WebElement, target_element: WebElement) -> None:
        """
         Perform a click and hold action chain on the source element, move it to the target element, and release it.

        :param source_element: The WebElement to click and hold.
        :param target_element: The WebElement to move to and release.
        :return: None.
        :raises NoSuchElementException: If the source or target element cannot be found.
        :raises ElementNotInteractableException: If the source or target element is not visible.
        :raises InvalidElementStateException: If the elements are not in a state where they can be interacted with.
        :raises StaleElementReferenceException: If the elements are no longer attached to the DOM.
        :raises TimeoutException: If the action takes too long to complete.
        :raises MoveTargetOutOfBoundsException: If the target element is outside the viewport.
        :raises WebDriverException: WebDriver encountered an error during performing click and hold action chain.
        """
        try:
            self.logger.info('Attempting to perform click and hold action chain.')
            actions = ActionChains(self.driver)
            actions.click_and_hold(source_element).move_to_element(target_element).release().perform()
            self.logger.info('Click and hold action chain is completed successfully.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found to perform click and hold action chain. Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform click and hold action chain. Error: {e}')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element is in an invalid state. Error: {e}')
            raise
        except StaleElementReferenceException as e:
            self.logger.error(f'Element is no longer attached to the DOM. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Action is timed out while performing click and hold action chain. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Target element is outside the viewport. Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing click and hold action chain. '
                              f'Error: {e}')
            raise

    def perform_double_click_action_chain(self, element: WebElement) -> None:
        """
        Perform double-click action chain on the specified web element.

        :param element: The WebElement to double-click.
        :return: None.
        :raises NoSuchElementException: If the element is not found in the DOM.
        :raises ElementNotInteractableException: If the element isn't interactable to perform double-click action chain.
        :raises TimeoutException: Timed out while performing double-click action chain.
        :raises WebDriverException: WebDriver encountered an error during performing double-click action chain.
        """
        try:
            self.logger.info('Attempting to perform double-click action.')
            actions = ActionChains(self.driver)
            actions.double_click(element).perform()
            self.logger.info('Double-click action chain is performed successfully.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found in the DOM to perform double-click action chain. Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform double-click action chain. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing double-click action chain. Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing double-click action chain. Error: {e}')

    def perform_drag_and_drop_action_chain(self, source_element: WebElement, target_element: WebElement) -> None:
        """
         Perform a drag-and-drop action chain.
        :param source_element: The WebElement to drag.
        :param target_element: The WebElement to drop the dragged element into.
        :return: None.
        :raises NoSuchElementException: If the source or target element isn't found perform drag and drop action chain.
        :raises ElementNotInteractableException: If the source or target element isn't interactable.
        :raises MoveTargetOutOfBoundsException: If the target element is outside the viewport or unreachable.
        :raises TimeoutException: Timed out while performing drag and drop action chain.
        :raises WebDriverException: WebDriver encountered an error during performing drag and drop action chain.
        """
        try:
            self.logger.info('Attempting to perform drag and drop action chain.')
            actions = ActionChains(self.driver)
            actions.drag_and_drop(source_element, target_element).perform()
            self.logger.info('Drag and drop action chain is performed successfully.')
        except NoSuchElementException as e:
            self.logger.error(f'Source or Target element isn\'t found to perform drag and drop action chain. '
                              f'Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform drag and drop action chain. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Target element is out of bounds for drag and drop action chain. Error: {e}')
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing drag and drop action chain. Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing drag and drop action chain. '
                              f'Error: {e}')
            raise

    def perform_hover_over_an_element_action_chain(self, element: WebElement) -> None:
        """
        Perform a hover (mouse over) action chain over the specified element.

        :param element: The WebElement to hover over.
        :return: None.
        :raises NoSuchElementException: If the element is not found in the DOM to perform hover over action chain.
        :raises ElementNotInteractableException: If the element isn't interactable to perform hover over action chain.
        :raises MoveTargetOutOfBoundsException: If the element is outside the viewport to perform hover over action chain.
        :raises TimeoutException: If the element takes too long to become interactable.
        :raises WebDriverException: WebDriver encountered an error during performing hover over an element action chain.
        """
        try:
            self.logger.info('Attempting to perform hover (mouse over) action chain.')
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.logger.info('Hover (mouse over) action chain is performed successfully.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found in the DOM to perform hover over action chain. Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform hover over action chain. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Element is out of bounds for hover over action chain. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing hover over action chain. Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing hover action chain. Error: {e}')
            raise

    def perform_context_click_action_chain(self, element: WebElement) -> None:
        """
        Perform a right-click (context-click) action chain on the specified element.

        :param element: The WebElement to perform the context-click on.
        :return: None.
        :raises NoSuchElementException: If the element is not found in the DOM to perform context-click action chain.
        :raises ElementNotInteractableException: If the element isn't interactable to perform context-click action chain.
        :raises MoveTargetOutOfBoundsException: If the element is outside the viewport to perform context-click action chain.
        :raises TimeoutException: If the element takes too long to become interactable.
        :raises WebDriverException: WebDriver encountered an error during performing context click action chain.

        """
        try:
            self.logger.info('Attempting to perform context click (right click) action chain.')
            actions = ActionChains(self.driver)
            actions.context_click(element).perform()
            self.logger.info('Context click (right click) action chain is performed successfully.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found in the DOM to perform context click action chain. Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element is interactable to perform context click action chain. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Element is out of bounds for context click action chain. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing context click action chain. Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing context click action chain. '
                              f'Error: {e}')
            raise
