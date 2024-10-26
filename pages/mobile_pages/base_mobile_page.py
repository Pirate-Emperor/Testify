from appium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import (NoSuchElementException, ElementNotInteractableException,
                                        InvalidElementStateException, StaleElementReferenceException,
                                        TimeoutException, WebDriverException, MoveTargetOutOfBoundsException)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder


class BaseMobilePage(BasePage):

    def __init__(self, driver: webdriver.Remote, timeout: int = 10):
        super().__init__(driver, timeout)

    def perform_tap_gesture_using_w3c_actions_api(self, element: WebElement, tap_type: str = 'single') -> None:
        """
        Perform a single or double tap gesture using the W3C Actions API.

        :param element:  A web element to perform a single or double tap gesture using the W3C Actions API.
        :param tap_type: Specifies the type of tap gesture: single or double. By default, it's single tap gesture.
        :return: None.
        :raises ValueError: If the provided tap_type is neither 'single' nor 'double'.
        :raises NoSuchElementException: If the element isn't found to perform a single or double tap gesture using
                                        the W3C Actions API.
        :raises ElementNotInteractableException: If the element isn't interactable to perform a single or double tap
                                                 gesture using the W3C Actions API.
        :raises InvalidElementStateException: If the element is not in a valid state to perform a single or double tap
                                              gesture using the W3C Actions API.
        :raises StaleElementReferenceException: If the element is no longer attached to the DOM to perform a single or
                                                double tap gesture using the W3C Actions API.
        :raises TimeoutException: If the single or double tap gesture takes too long to perform using
                                  the W3C Actions API.
        :raises WebDriverException: If WebDriver encounters an error while performing a single or double tap gesture
                                    using the W3C Actions API.
        """
        try:
            self.logger.info('Getting the current location of the element.')
            element_location = element.location
            self.logger.info(f'Current location of the element: {element_location}')
            self.logger.info(f'Performing a {tap_type} tap gesture using the W3C Actions API')
            if tap_type.lower() == 'single':
                self.driver.tap([(element_location['x'], element_location['y'])])
            elif tap_type.lower() == 'double':
                self.driver.tap([(element_location['x'], element_location['y'])])
                self.driver.tap([(element_location['x'], element_location['y'])])
            else:
                self.logger.error(f'Unsupported tap type: {tap_type}. Supported values are "single" and "double".')
                raise ValueError(f'Tap type {tap_type} is not supported.')
            self.logger.info(f'The {tap_type} tap gesture is performed successfully using the W3C Actions API.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found to perform a {tap_type} tap gesture using the W3C Actions API. '
                              f'Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform a {tap_type} tap gesture using the '
                              f'W3C Actions API. Error: {e}')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element isn\'t in a valid state to perform a {tap_type} tap gesture using '
                              f'the W3C Actions API. Error: {e}')
            raise
        except StaleElementReferenceException as e:
            self.logger.error(f'Element is no longer attached to the DOM to perform a {tap_type} tap gesture '
                              f'using the W3C Actions API. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timeout occurred while performing a {tap_type} tap gesture using the W3C Actions API. '
                              f'Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing a {tap_type} tap gesture using '
                              f'the W3C Actions API. Error: {e}.')
            raise

    def perform_tap_gesture_using_w3c_mobile_gestures_commands(self, element: WebElement,
                                                               tap_type: str = 'single') -> None:
        """
        Perform a single or double tap gesture using the W3C Mobile Gestures Commands.

        :param element:  The web element to perform tap gesture.
        :param tap_type: Specifies the type of tap gesture: single or double. By default, it's single tap gesture.
        :return: None.
        :raises ValueError: If the provided tap_type is neither 'single' nor 'double'.
        :raises NoSuchElementException: If the element isn't found to perform a single or double tap gesture using the
                                        W3C Mobile Gestures Commands.
        :raises ElementNotInteractableException: If the element isn't interactable to perform a single or double tap
                                                 gesture using the W3C Mobile Gestures Commands.
        :raises InvalidElementStateException: If the element isn't in a valid state to perform a single or double tap
                                              gesture using the W3C Mobile Gestures Commands.
        :raises StaleElementReferenceException: If the element is no longer attached to the DOM to perform a single or
                                                double tap gesture using the W3C Mobile Gestures Commands.
        :raises TimeoutException: If the single or double tap gesture takes too long to perform using the W3C Mobile
                                  Gestures Commands.
        :raises WebDriverException: If WebDriver encounters an error while performing a single or double tap gesture
                                    using the W3C Mobile Gestures Commands.
        """
        try:
            self.logger.info('Retrieving the current location of the element.')
            element_location = element.location
            self.logger.info(f'Element is located at: {element_location}')
            if tap_type.lower() not in ['single', 'double']:
                self.logger.error(f'Unsupported tap type: {tap_type}. Supported values are "single" and "double".')
                raise ValueError(f'Unsupported tap type: {tap_type}. Supported values are "single" and "double".')
            self.logger.info(f'Performing a {tap_type} tap gesture using the Mobile Gestures Command.')
            self.driver.execute_script(
                f'mobile: {tap_type}', {
                    'x': element_location['x'],
                    'y': element_location['y']
                }
            )
            self.logger.info(f'{tap_type.capitalize()} tap gesture successfully performed using the W3C Mobile Gestures'
                             f' Commands.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found to perform a {tap_type} tap gesture using the W3C Mobile Gestures '
                              f'Commands. Error: {e}.')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform a {tap_type} tap gesture using the W3C Mobile '
                              f'Gestures Commands. Error: {e}.')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element is in an invalid state to perform a {tap_type} tap gesture using the W3C Mobile'
                              f' Gestures Commands. Error: {e}.')
            raise
        except StaleElementReferenceException as e:
            self.logger.error(f'Element is no longer attached to the DOM to perform a {tap_type} tap gesture using the '
                              f'W3C Mobile Gestures Commands. Error: {e}.')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out occurred while performing a {tap_type} tap gesture using the W3C Mobile '
                              f'Gestures Commands. Error: {e}.')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing a {tap_type} tap gesture using the '
                              f'W3C Mobile Gestures Commands. Error: {e}.')
            raise

    def perform_drag_and_drop_gesture_using_w3c_actions_api(self, draggable_element: WebElement,
                                                            droppable_element: WebElement) -> None:
        """
        Perform a drag and drop gesture using the W3C Actions API.

        :param draggable_element: the element to be dragged.
        :param droppable_element: the element to drop the draggable element onto.
        :return: None.
        :raises NoSuchElementException: If the draggable or droppable element isn't found to perform drag and drop
                                        gesture using the W3C Actions API.
        :raises StaleElementReferenceException: If the elements are no longer attached to the DOM to perform drag and
                                                drop gesture using the W3C Actions API.
        :raises ElementNotInteractableException: If the draggable or droppable element isn't interactable to perform a
                                                 drag and drop gesture using the W3C Actions API.
        :raises InvalidElementStateException: If the elements aren't in a state to perform a drag and drop gesture using
                                              the W3C Actions API.
        :raises TimeoutException: If the drag-and-drop gesture takes too long to perform using the W3C Actions API.
        :raises MoveTargetOutOfBoundsException: If the target element is outside the viewport to perform a drag and drop
                                                gesture using the W3C Actions API.
        :raises WebDriverException: If WebDriver encounters an error while performing a drag and drop gesture.
        """
        try:
            self.logger.info("Performing drag and drop action using W3C Actions API.")
            self.driver.drag_and_drop(draggable_element, droppable_element)
            self.logger.info("Drag and drop is performed successfully using W3C Actions API.")
        except NoSuchElementException as e:
            self.logger.error(f'Draggable or droppable element isn\'t found to perform a drag and drop gesture using '
                              f'the W3C Actions API. Error: {e}.')
            raise
        except StaleElementReferenceException as e:
            self.logger.error(f'Element is no longer attached to the DOM to perform a drag and drop gesture using '
                              f'the W3C Actions API. Error {e}.')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform a drag and drop gesture using the '
                              f'W3C Actions API. Error: {e}')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element is in an invalid state to perform a drag and drop gesture using the '
                              f'W3C Actions API. Error: {e}.')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing drag and drop gesture using the W3C Actions API. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Target element is outside the viewport to perform a drag and drop gesture using '
                              f'the W3C Actions API. Error: {e}.')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing a drag and drop gesture using '
                              f'the W3C Actions API. Error: {e}.')

    def perform_drag_and_drop_using_w3c_mobile_gestures_commands(self, draggable_element: WebElement,
                                                                 droppable_element: WebElement) -> None:
        """
        Perform a drag and drop gesture using the W3C Mobile Gestures Commands.

        :param draggable_element: the element to be dragged.
        :param droppable_element: the element to drop the draggable element onto.
        :return: None.
        :raises NoSuchElementException: If the element isn't found to perform a drag and drop gesture using the W3C
                                        Mobile Gestures Commands.
        :raises StaleElementReferenceException: If the element is no longer attached to the DOM to perform a drag and
                                                drop gesture using the W3C Mobile Gestures Commands.
        :raises ElementNotInteractableException: If the element isn't interactable to perform a drag and drop gesture
                                                 using the W3C Mobile Gestures Commands.
        :raises InvalidElementStateException: If the element in a state where it can't perform a drag and drop gesture
                                              using the W3C Mobile Gestures Commands.
        :raises TimeoutException: If the drag and drop gesture takes too long to perform using the W3C Mobile Gestures
                                  Commands.
        :raises MoveTargetOutOfBoundsException: If element is outside the viewport to perform a drag and drop gesture
                                                using the W3C Mobile Gestures Commands.
        :raises WebDriverException: If WebDriver encounters an error while performing a drag and drop gesture using W3C
                                    Mobile Gestures Commands.
        """
        try:
            self.logger.info("Performing drag and drop gesture using the W3C Mobile Gestures Commands.")
            self.driver.execute_script(
                'mobile: dragGesture', {
                    'elementId': draggable_element,
                    'endX': droppable_element.location['x'],
                    'endY': droppable_element.location['y']
                }
            )
            self.logger.info("Drag and drop gesture is performed successfully using the W3C Mobile Gestures Commands.")
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found to perform a drag and drop gesture using the W3C Mobile Gestures '
                              f'Commands. Error: {e}.')
            raise
        except StaleElementReferenceException as e:
            self.logger.error(f'Element is no longer attached to the DOM to perform a drag and drop gesture using '
                              f'the W3C Mobile Gestures Commands. Error: {e}.')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform a drag and drop gesture using the W3C Mobile '
                              f'Gestures Commands. Error: {e}.')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element is in an invalid state to perform a drag and drop gesture using the W3C Mobile'
                              f'Gestures Commands. Error: {e}.')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing a drag and drop gesture using the W3C Mobile Gestures '
                              f'Commands. Error: {e}.')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Target element is outside the viewport to perform a drag and drop gesture using the '
                              f'W3C Mobile Gestures Commands. Error: {e}.')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing a drag and drop gesture using the '
                              f'W3C Mobile Gestures Commands. Error: {e}.')

    def perform_long_press_gesture_using_w3c_actions_api(self, element: WebElement) -> None:
        """
        Perform a long press (Press and Hold) gesture using the W3C Actions API.

        :param element: The WebElement to perform the long press gesture using the W3C Actions API.
        :return: None.
        :raises NoSuchElementException: If the element isn't found to perform the long press gesture using
                                        the W3C Actions API.
        :raises ElementNotInteractableException: If the element isn't interactable to perform the long press gesture
                                                 using the W3C Actions API.
        :raises InvalidElementStateException: If the element is not in a valid state to perform the long press gesture
                                              using the W3C Actions API.
        :raises MoveTargetOutOfBoundsException: If the element is outside the viewport to perform a long press gesture
                                                using the W3C Actions API.
        :raises TimeoutException: If the long press gesture takes too long to perform using the W3C Actions API.
        :raises WebDriverException: If WebDriver encounters an error while performing the long press gesture using
                                    the W3C Actions API.
        """
        try:
            self.logger.info('Creating an instance from ActionChains Class.')
            actions = ActionChains(self.driver)
            self.logger.info('Creating a touch type of pointer input for gesture.')
            touch_input = PointerInput(interaction.POINTER_TOUCH, 'touch')
            self.logger.info('Overriding the pointer action to specify touch input.')
            actions.w3c_actions = ActionBuilder(self, mouse=touch_input)
            self.logger.info('Performing long press gesture using the W3C Actions API.')
            actions.w3c_actions.pointer_action.click_and_hold(element)
            actions.perform()
            self.logger.info('The long press gesture was successfully performed using the W3C Actions API.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found to perform a long press gesture using the W3C Actions API. '
                              f'Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform a long press gesture using the W3C Actions API. '
                              f'Error: {e}')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element is in an invalid state for performing a long press gesture using '
                              f'the W3C Actions API. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Element is outside the viewport to perform a long press gesture using '
                              f'the W3C Actions API. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing a long press gesture using the W3C Actions API. Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing a long press gesture using '
                              f'the W3C Actions API. Error: {e}')
            raise

    def perform_long_press_gesture_using_w3c_mobile_gestures_commands(self, element: WebElement,
                                                                      duration: int = 1000) -> None:
        """
         Perform a long press gesture using the W3C Mobile Gestures Commands.
        :param element: The WebElement to perform the long press gesture using the W3C Mobile Gestures Commands.
        :param duration: The duration of the long press gesture in milliseconds (default is 1000 ms).
        :return: None.
        :raises NoSuchElementException: If the element isn't found to perform the long press gesture using
                                        the W3C Mobile Gestures Commands.
        :raises ElementNotInteractableException: If the element isn't interactable to perform the long press gesture
                                                 using the W3C Mobile Gestures Commands.
        :raises InvalidElementStateException: If the element is not in a valid state to perform the long press gesture
                                              using the W3C Mobile Gestures Commands.
        :raises MoveTargetOutOfBoundsException: If the element is outside the viewport to perform a long press gesture
                                                using the W3C Mobile Gestures Commands.
        :raises TimeoutException: If the long press gesture takes too long to perform using the W3C Mobile Gestures
                                  Commands.
        :raises WebDriverException: If WebDriver encounters an error during the execution of the long press gesture
                                    using the W3C Mobile Gestures Commands.
        """
        try:
            self.logger.info('Retrieving the current location of the element')
            element_location = element.location
            self.logger.info(f'Element located at: {element_location}')
            self.logger.info('Performing long press gesture using the W3C Mobile Gestures Commands.')
            self.driver.execute_script(
                'mobile: longClickGesture',
                {'x': element_location['x'],
                 'y': element_location['y'], 'duration': duration})
            self.logger.info('The long press gesture was successfully performed using the W3C Mobile Gestures '
                             'Commands.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found to perform a long press gesture using the W3C Mobile Gestures '
                              f'Commands. Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform a long press gesture using the '
                              f'W3C Mobile Gestures Commands. Error: {e}')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element is in an invalid state for performing a long press gesture using '
                              f'the W3C Mobile Gestures Commands. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Element is outside the viewport to perform a long press gesture using the '
                              f'W3C Mobile Gestures Commands. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing a long press gesture using the W3C Mobile Gestures Commands.'
                              f' Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing a long press gesture using '
                              f'the W3C Mobile Gestures Commands. Error: {e}')
            raise

    def perform_scroll_gesture_using_w3c_actions_api(self, start_element: WebElement, end_element: WebElement,
                                                     scroll_direction: str = 'up') -> None:
        """
        Perform a scroll up, down, left, or right gesture between two elements using the W3C Actions API.

        :param start_element: The WebElement where the scroll gesture starts.
        :param end_element: The WebElement where the scroll gesture ends.
        :param scroll_direction: The type of scroll gesture to perform. Options are 'up', 'down', 'left', or 'right'.
                            Default is 'up'.
        :return: None.
        :raises ValueError: If an unsupported scroll direction is provided.
        :raises NoSuchElementException: If either start_element or end_element isn't found to perform scroll gesture
                                        using the W3C Actions API.
        :raises ElementNotInteractableException: If the start or end elements are not interactable to perform scroll
                                                 gesture using the W3C Actions API.
        :raises InvalidElementStateException: If the element is not in a valid state to perform the scroll gesture
                                              using the W3C Actions API.
        :raises MoveTargetOutOfBoundsException: If the start or end element is outside the viewport to perform scroll
                                                gesture using the W3C Actions API.
        :raises TimeoutException: If the scroll gesture takes too long to perform using the W3C Actions API.
        :raises WebDriverException: If WebDriver encounters an error while performing the scroll gesture using the
                                    W3C Actions API.
        """
        try:
            if scroll_direction.lower() == 'down' or scroll_direction.lower() == 'right':
                self.logger.info(f'Performing scroll {scroll_direction} gesture using the W3C Actions API.')
                self.driver.scroll(origin_el=end_element, destination_el=start_element)
                self.logger.info(f'The scroll {scroll_direction} was successfully performed using the W3C Actions API.')
            elif scroll_direction.lower() == 'up' or scroll_direction.lower() == 'left':
                self.logger.info(f'Performing scroll {scroll_direction} gesture using the W3C Actions API.')
                self.driver.scroll(origin_el=start_element, destination_el=end_element)
                self.logger.info(f'The scroll {scroll_direction} was successfully performed using the W3C Actions API.')
            else:
                self.logger.error(f'Unsupported scroll type provided: {scroll_direction}. Must be "up", "down", "left",'
                                  f'or "right".')
                raise ValueError(f'Scroll type {scroll_direction} is not supported.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found to perform scroll {scroll_direction} gesture using '
                              f'the W3C Actions API. Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform scroll {scroll_direction} gesture using '
                              f'the W3C Actions API. Error: {e}')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element is in an invalid state for performing scroll {scroll_direction} gesture using '
                              f'the W3C Actions API. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Element is outside the viewport to perform scroll {scroll_direction} gesture using the '
                              f'W3C Actions API. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing scroll {scroll_direction} gesture using '
                              f'the W3C Actions API. Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(f'WebDriver encountered an error during performing scroll {scroll_direction} gesture '
                              f'using the W3C Actions API. Error: {e}')
            raise

    def perform_scroll_gesture_using_w3c_mobile_gestures_commands(self, element_id: WebElement,
                                                                  scroll_direction: str = 'up', percent: float = 0.5,
                                                                  speed: int = 1000) -> None:
        """
        Perform a scroll up, down, left, or right gesture using W3C Mobile Gestures Commands.

        :param element_id: The id of the element to be scrolled.
        :param scroll_direction: Scrolling direction. Options are 'up', 'down', 'left', or 'right'. Default is 'up'.
        :param percent: The size of the scroll as a percentage of the scrolling area size. Valid values must be float
                        numbers greater than zero
        :param speed: The speed at which to perform this gesture in pixels per second. The value must not be negative.
        :return: None.
        :raises ValueError: If the percent value is less than or equal to zero, or if speed is negative, or Invalid
                            scroll direction value.
        :raises NoSuchElementException: If the element is not found to perform scroll gesture using W3C Mobile
                                        Gestures Commands.
    :raises ElementNotInteractableException: If the element is not interactable to perform scroll gesture using W3C
                                             Mobile Gestures Commands.
    :raises InvalidElementStateException: If the element is in an invalid state to perform scroll gesture using W3C
                                          Mobile Gestures Commands.
    :raises MoveTargetOutOfBoundsException: If the element is outside the viewport to perform scroll gesture using
                                            W3C Mobile Gestures Commands.
    :raises TimeoutException: If the scroll gesture takes too long time to perform using the W3C Mobile Gestures
                              Commands.
    :raises WebDriverException: If WebDriver encounters an error while performing the scroll gesture using the W3C
                                Mobile Gestures Commands.
        """
        try:
            if percent <= 0:
                raise ValueError(f'Invalid percent value: {percent}. Percent must be greater than 0.')
            if speed < 0:
                raise ValueError(f'Invalid speed value: {speed}. Speed must be a non-negative integer.')
            if scroll_direction.lower() not in ['up', 'down', 'left', 'right']:
                raise ValueError(f'Invalid scroll direction value: {scroll_direction}.')
            self.logger.info(f'Performing scroll {scroll_direction} gesture using the W3C Mobile Gestures Commands.')
            self.driver.execute_script(
                'mobile: scrollGesture', {
                    'elementId': element_id,
                    'direction': scroll_direction,
                    'percent': percent,
                    'speed': speed
                }
            )
            self.logger.info(f'The scroll {scroll_direction} was successfully performed using the W3C Mobile Gestures '
                             f'Commands.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found to perform scroll {scroll_direction} gesture using '
                              f'the W3C Mobile Gestures Commands. Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform scroll {scroll_direction} gesture using '
                              f'the W3C Mobile Gestures Commands. Error: {e}')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element is in an invalid state for performing scroll {scroll_direction} gesture using '
                              f'the W3C Mobile Gestures Commands. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Element is outside the viewport to perform scroll {scroll_direction} gesture using the '
                              f'W3C Mobile Gestures Commands. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing scroll {scroll_direction} gesture using '
                              f'the W3C Mobile Gestures Commands. Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(
                f'WebDriver encountered an error during performing scroll {scroll_direction} gesture using '
                f'the W3C Mobile Gestures Commands. Error: {e}')
            raise

    def perform_swipe_gesture_using_w3c_actions_api(self, start_element: WebElement, end_element: WebElement,
                                                    swipe_direction: str = 'up') -> None:
        """
        Perform a swipe up, down, left, or right gesture using the W3C Actions API.

        :param start_element: The WebElement where the swipe gesture starts.
        :param end_element: The WebElement where the swipe gesture ends.
        :param swipe_direction: The direction of the swipe gesture. Options are 'up' or 'down'. Default is 'up'.
        :return: None.
        :raises ValueError: If an unsupported swipe direction is provided.
        :raises NoSuchElementException: If either start_element or end_element isn't found to perform swipe gesture
                                        using the W3C Actions API.
        :raises ElementNotInteractableException: If the start or end elements are not interactable to perform swipe
                                                 gesture using the W3C Actions API.
        :raises InvalidElementStateException: If the element is not in a valid state to perform the swipe gesture
                                              using the W3C Actions API.
        :raises MoveTargetOutOfBoundsException: If the start or end element is outside the viewport to perform swipe
                                                gesture using the W3C Actions API.
        :raises TimeoutException: If the swipe gesture takes too long to perform using the W3C Actions API.
        :raises WebDriverException: If WebDriver encounters an error while performing the swipe gesture using the
                                    W3C Actions API.
        """
        try:
            self.logger.info(f'Getting the location of the start element: {start_element}')
            start_element_location = start_element.location
            self.logger.info(f'Start element is located at: {start_element_location}')
            self.logger.info(f'Getting the location of the end element: {end_element}')
            end_element_location = end_element.location
            self.logger.info(f'End element is located at: {end_element_location}')
            if swipe_direction == 'up' or swipe_direction == 'left':
                self.logger.info(f'Performing swipe {swipe_direction} gesture using the W3C Actions API.')
                self.driver.swipe(start_x=end_element_location['x'], start_y=end_element_location['y'],
                                  end_x=start_element_location['x'], end_y=start_element_location['y'])
                self.logger.info(f'Swipe {swipe_direction} gesture was successfully performed using the W3C Actions '
                                 f'API.')
            elif swipe_direction == 'down' or swipe_direction == 'right':
                self.logger.info(f'Performing swipe {swipe_direction} gesture using the W3C Actions API.')
                self.driver.swipe(start_x=start_element_location['x'], start_y=start_element_location['y'],
                                  end_x=end_element_location['x'], end_y=end_element_location['y'])
                self.logger.info(f'Swipe {swipe_direction} gesture was successfully performed using the W3C Actions '
                                 f'API.')
            else:
                self.logger.error(f'Invalid swipe direction value: {swipe_direction}. Options are up, or down')
                raise ValueError('Invalid swipe direction value. Options are up, down, left, or right.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found to perform swipe {swipe_direction} gesture using the W3C Actions '
                              f'API. Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform swipe {swipe_direction} gesture using the W3C '
                              f'Actions API. Error: {e}')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element is in an invalid state for performing swipe {swipe_direction} gesture using '
                              f'the W3C Actions API. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Element is outside the viewport to perform swipe {swipe_direction} gesture using the '
                              f'W3C Actions API. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing swipe {swipe_direction} gesture using the W3C Actions API. '
                              f'Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(
                f'WebDriver encountered an error during performing swipe {swipe_direction} gesture using the W3C '
                f'Actions API. Error: {e}')
            raise

    def perform_swipe_up_gesture_using_w3c_mobile_gestures_commands(self, element_id: WebElement,
                                                                    swipe_direction: str = 'up', percent: float = 0.3,
                                                                    speed: int = 3000) -> None:
        """
        Perform a swipe up, down, left, or right gesture using the W3C Mobile Gestures Commands.
        :param element_id: The WebElement to be swiped.
        :param swipe_direction: The direction of the swipe gesture. Options are 'up', 'down', 'right', 'left'.
                                Default is 'up'.
        :param percent: The size of the swipe as a percentage of the swipe area size. Must be in range 0..1.
                        Example: 1.0 is 100%.
        :param speed: The speed at which to perform this gesture in pixels per second. Must be non-negative.
        :return: None.
        :raises ValueError: If the swipe direction, percent, or speed are invalid.
        :raises NoSuchElementException: If either start_element or end_element isn't found to perform swipe gesture
                                        using the W3C Mobile Gestures Commands.
        :raises ElementNotInteractableException: If the start or end elements are not interactable to perform swipe
                                                 gesture using the W3C Mobile Gestures Commands.
        :raises InvalidElementStateException: If the element is not in a valid state to perform the swipe gesture
                                              using the W3C Mobile Gestures Commands.
        :raises MoveTargetOutOfBoundsException: If the start or end element is outside the viewport to perform swipe
                                                gesture using the W3C Mobile Gestures Commands.
        :raises TimeoutException: If the swipe gesture takes too long to perform using the W3C Mobile Gestures Commands.
        :raises WebDriverException: If WebDriver encounters an error while performing the swipe gesture using the W3C
                                    Mobile Gestures Commands.
        """
        try:
            if swipe_direction.lower() not in ['up', 'down', 'left', 'right']:
                self.logger.error('Invalid swipe direction value. Options are up, down, left, or right.')
                raise ValueError('Invalid swipe direction value. Options are up, down, left, or right.')
            if not (0 <= percent <= 1):
                self.logger.error(f'Invalid percent value: {percent}. Must be in range 0..1.')
                raise ValueError(f'Invalid percent value: {percent}. Must be in range 0..1.')
            if speed < 0:
                self.logger.error(f'Invalid speed value: {speed}. Speed must be a non-negative integer.')
                raise ValueError(f'Invalid speed value: {speed}. Speed must be a non-negative integer.')
            self.logger.info(f'Performing swipe {swipe_direction} gesture using the W3C Mobile Gestures Commands.')
            self.driver.execute_script(
                'mobile: swipeGesture', {
                    'elementId': element_id,
                    'direction': swipe_direction,
                    'percent': percent,
                    'speed': speed
                }
            )
            self.logger.info(f'Successfully performed swipe {swipe_direction} gesture using the W3C Mobile Gestures '
                             f'Commands.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found to perform swipe {swipe_direction} gesture using the W3C Mobile '
                              f'Gestures. Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform swipe {swipe_direction} gesture using the W3C '
                              f'Mobile Gestures. Error: {e}')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element is in an invalid state for performing swipe {swipe_direction} gesture using '
                              f'the W3C Mobile Gestures. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Element is outside the viewport to perform swipe {swipe_direction} gesture using the '
                              f'W3C Mobile Gestures. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing swipe {swipe_direction} gesture using the W3C Mobile '
                              f'Gestures. Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(
                f'WebDriver encountered an error during performing swipe {swipe_direction} gesture using the W3C '
                f'Mobile Gestures. Error: {e}')
            raise

    def perform_flick_gesture_using_w3c_actions_api(self, start_element: WebElement, end_element: WebElement,
                                                    flick_direction: str) -> None:
        """
        Perform a flick up or down gesture using the W3C Actions API.

        :param start_element: The WebElement where the flick gesture starts.
        :param end_element: The WebElement where the flick gesture ends.
        :param flick_direction: The direction of the flick gesture. Options are 'left', or 'right'.
        :return: None.
        :raises ValueError: If the flick direction is invalid.
        :raises NoSuchElementException: If either start_element or end_element isn't found to perform flick gesture
                                        using the W3C Actions API.
        :raises ElementNotInteractableException: If the start or end elements are not interactable to perform flick
                                                 gesture using the W3C Actions API.
        :raises InvalidElementStateException: If the element is not in a valid state to perform the flick gesture
                                              using the W3C Actions API.
        :raises MoveTargetOutOfBoundsException: If the start or end element is outside the viewport to perform flick
                                                gesture using the W3C Actions API.
        :raises TimeoutException: If the flick gesture takes too long to perform using the W3C Actions API.
        :raises WebDriverException: If WebDriver encounters an error while performing the flick gesture using the W3C
                                    Actions API.
        """
        try:
            self.logger.info('Retrieving the location of the start element')
            start_element_location = start_element.location
            self.logger.info(f'Start element located at: {start_element_location}')
            self.logger.info('Retrieving the location of the end element')
            end_element_location = end_element.location
            self.logger.info(f'End element located at: {end_element_location}')
            if flick_direction.lower() == 'up':
                self.logger.info('Performing flick up gesture using the W3C Actions API.')
                self.driver.flick(start_x=end_element_location['x'], start_y=end_element_location['y'],
                                  end_x=start_element_location['x'], end_y=start_element_location['y'])
                self.logger.info('Flick up gesture was successfully performed using the W3C Actions API.')
            elif flick_direction.lower() == 'down':
                self.logger.info('Performing flick down gesture using the W3C Actions API.')
                self.driver.flick(start_x=start_element_location['x'], start_y=start_element_location['y'],
                                  end_x=end_element_location['x'], end_y=end_element_location['y'])
                self.logger.info('Flick down gesture was successfully performed using the W3C API Actions API.')
            else:
                self.logger.error('Invalid flick direction value. Options are up, down, left, or right.')
                raise ValueError('Invalid flick direction value. Options are up, down, left, or right.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found to perform flick {flick_direction} gesture using the W3C API '
                              f'Actions API. Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform flick {flick_direction} gesture using the W3C '
                              f'API Actions API. Error: {e}')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element is in an invalid state for performing flick {flick_direction} gesture using '
                              f'the W3C API Actions API. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Element is outside the viewport to perform flick {flick_direction} gesture using the '
                              f'W3C API Actions API. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing flick {flick_direction} gesture using the W3C API Actions '
                              f'API. Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(
                f'WebDriver encountered an error during performing flick {flick_direction} gesture using the W3C API '
                f'Actions API. Error: {e}')
            raise

    def perform_flick_gesture_using_w3c_mobile_gestures_commands(self, element_id: WebElement, flick_direction: str,
                                                                 percent: float) -> None:
        """

        :param element_id:
        :param flick_direction:
        :param percent:
        :return:
        """
        try:
            if flick_direction.lower() not in ['up', 'down']:
                self.logger.error('Invalid flick direction value. Options are up, or down.')
                raise ValueError('Invalid flick direction value. Options are up, or down.')
            if not (0 <= percent <= 1):
                self.logger.error(f'Invalid percent value: {percent}. Must be in range 0..1.')
                raise ValueError(f'Invalid percent value: {percent}. Must be in range 0..1.')
            self.logger.info(f'Performing flick {flick_direction} gesture using the W3C Mobile Gestures Commands.')
            self.driver.execute_script(
                'mobile: flingGesture', {
                    'elementId': element_id,
                    'direction': flick_direction,
                    'percent': percent
                }
            )
            self.logger.info(f'Flick {flick_direction} gesture was successfully performed using the W3C Mobile '
                             f'Gestures Commands.')
        except NoSuchElementException as e:
            self.logger.error(f'Element isn\'t found to perform flick {flick_direction} gesture using the W3C Mobile '
                              f'Gestures Commands. Error: {e}')
            raise
        except ElementNotInteractableException as e:
            self.logger.error(f'Element isn\'t interactable to perform flick {flick_direction} gesture using the W3C '
                              f'Mobile Gestures Commands. Error: {e}')
            raise
        except InvalidElementStateException as e:
            self.logger.error(f'Element is in an invalid state for performing flick {flick_direction} gesture using '
                              f'the W3C Mobile Gestures Commands. Error: {e}')
            raise
        except MoveTargetOutOfBoundsException as e:
            self.logger.error(f'Element is outside the viewport to perform flick {flick_direction} gesture using the '
                              f'W3C Mobile Gestures Commands. Error: {e}')
            raise
        except TimeoutException as e:
            self.logger.error(f'Timed out while performing flick {flick_direction} gesture using the W3C Mobile '
                              f'Gestures Commands. Error: {e}')
            raise
        except WebDriverException as e:
            self.logger.error(
                f'WebDriver encountered an error during performing flick {flick_direction} gesture using the W3C '
                f'Mobile Gestures Commands. Error: {e}')
            raise
