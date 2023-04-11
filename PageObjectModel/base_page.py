import sys
from traceback import print_stack

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import traceback

from GenericUtil import configure_log


class BasePage:
    log = configure_log.get_logger_instance()

    def __int__(self, driver):
        self.driver = driver

    def get_webdriver_wait_instance(self):
        wait = WebDriverWait(self.driver,10)
        return wait

    def get_select_class_instance(self, element):
        select = Select(element)
        return select

    def get_action_chain_instance(self):
        action = ActionChains(self.driver)
        return action

    def get_alert_class_instance(self):
        alert = Alert(self.driver)
        return alert

    def get_switch_to_instance(self):
        return self.driver.switch_to

    def highlight(element):
        """Highlights (blinks) a Selenium Webdriver element"""
        driver = element._parent

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                  element, s)

        original_style = element.get_attribute('style')
        apply_style("border: 2px solid red;")
        time.sleep(.3)
        apply_style(original_style)

    def get_element(self, *args):
        try:
            element = self.driver.find_element(*args)

            self.log.info(f"The element with locator type: {args[0]} and locator: {args[1]} was found")
            return element
        except Exception as e:
            self.log.error(e)
            # print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to locate element in the DOM"

    def get_elements(self, *args):
        try:
            elements = self.driver.find_elements(*args)
            self.log.info(f"The elements with locator type: {args[0]} and locator: {args[1]} was found")
            return elements
        except Exception as e:
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to locate elements in the DOM"

    def click(self, *args):
        try:
            element = self.get_element(*args)
            self.get_webdriver_wait_instance().until(ec.element_to_be_clickable(element))
            element.click()
            self.log.info(
                f"Performing click action on element with locator type: {args[0]} and locator: {args[1]}")
        except Exception as e:
            print(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to perform click action on the element"

    def send_keys(self, *args, value=None):
        try:
            element = self.get_element(*args)
            self.get_webdriver_wait_instance().until(ec.element_to_be_clickable(element))
            element.send_keys(value)
            self.log.info(
                f"Performing send keys action on element with locator type: {args[0]} and locator: {args[1]} and value entered is: {value}")
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to perform send keys action on the element"

    def select_by_index(self, *args, index):
        try:
            element = self.get_element(*args)
            self.get_select_class_instance(element).select_by_index(index)
            self.log.info(
                f"Performing select action from dropdown with locator type: {args[0]} and locator: {args[1]} and the "
                f"index is: {index}")

        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to perform select action on the dropdown"

    def select_by_value(self, *args, value=None):
        try:
            element = self.get_element(*args)
            self.get_select_class_instance(element).select_by_value(value)
            self.log.info(
                f"Performing select action from dropdown with locator type: {args[0]} and locator: {args[1]} and the "
                f"value is: {value}")

        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to perform select action on the dropdown"

    def select_by_text(self, *args, text):
        try:
            element = self.get_element(*args)
            self.get_select_class_instance(element).select_by_visible_text(text)
            self.log.info(
                f"Performing select action from dropdown with locator type: {args[0]} and locator: {args[1]} and the "
                f"text is: {text}")

        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to perform select action on the dropdown"

    def get_alert_text(self):
        try:
            self.get_webdriver_wait_instance().until(ec.alert_is_present())
            alert = self.get_alert_class_instance()
            alert_text = alert.text
            self.log.info(
                f"The text present in the alert is: {alert_text}")
            return alert_text
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to fetch text from the alert"

    def accept_alert(self):
        try:
            self.get_webdriver_wait_instance().until(ec.alert_is_present())
            alert = self.get_alert_class_instance()
            alert_text = alert.text
            alert.accept()
            self.log.info(
                f"The text present in the alert is: {alert_text} and accepting the alert")
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to fetch text from the alert and accept the alert"

    def dismiss_alert(self):
        try:
            self.get_webdriver_wait_instance().until(ec.alert_is_present())
            alert = self.get_alert_class_instance()
            alert_text = alert.text
            alert.dismiss()
            self.log.info(
                f"The text present in the alert is: {alert_text} and dismissing the alert")
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to fetch text from the alert and dismiss the alert"

    def send_key_to_alert_and_accept(self, text):
        try:
            self.get_webdriver_wait_instance().until(ec.alert_is_present())
            alert = self.get_alert_class_instance()
            alert_text = alert.text
            alert.send_keys(text)
            alert.accept()
            self.log.info(
                f"The text present in the alert is: {alert_text}, entering text to the alert: {text} and accepting "
                f"the alert")
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to fetch text from the alert, enter value and accept the alert"

    def send_key_to_alert_and_dismiss(self, text):
        try:
            self.get_webdriver_wait_instance().until(ec.alert_is_present())
            alert = self.get_alert_class_instance()
            alert_text = alert.text
            alert.send_keys(text)
            alert.dismiss()
            self.log.info(
                f"The text present in the alert is: {alert_text}, entering text to the alert: {text} and dismissing "
                f"the alert")
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to fetch text from the alert, enter value and dismiss the alert"

    def move_to_element(self, *args):
        try:
            element = self.get_element(*args)
            # self.get_webdriver_wait_instance().until(ec.presence_of_element_located(element))
            self.get_action_chain_instance().move_to_element(element).perform()
            self.log.info(
                f"Performing mouse hover action on element with locator type: {args[0]} and locator: {args[1]}")
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to perform mouse hover action on the element"

    def right_click(self, *args):
        try:
            element = self.get_element(*args)
            self.get_webdriver_wait_instance().until(ec.presence_of_element_located(element))
            self.get_action_chain_instance().context_click(element).perform()
            self.log.info(
                f"Performing right click action on element with locator type: {args[0]} and locator: {args[1]}")
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to perform right click action on the element"

    def drag_and_drop(self, draggable_ele, droppable_ele):
        try:
            draggable_element = self.get_element(draggable_ele)
            self.get_webdriver_wait_instance().until(ec.presence_of_element_located(draggable_element))
            droppable_element = self.get_element(droppable_ele)
            self.get_webdriver_wait_instance().until(ec.presence_of_element_located(droppable_element))
            self.get_action_chain_instance().drag_and_drop(draggable_element, droppable_element).perform()
            self.log.info("The drag and drop was performed successfully")
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "The drag and drop was performed un-successfully"

    def move_slider_horizontally(self, *args, offset_percentage):
        try:
            slider_element = self.get_element(*args)
            ele_position = slider_element.size
            width = ele_position["width"]
            x_offset = ((offset_percentage) / 100) * width
            self.get_action_chain_instance().move_to_element_with_offset(slider_element, x_offset, 0).perform()
        except Exception as e:
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])

    def drag_and_drop_offset(self, *args, x_offset=0, y_offset=0):
        try:
            slider_element = self.get_element(*args)
            self.get_action_chain_instance().move_to_element_with_offset(slider_element, x_offset, y_offset).perform()
            self.log.info(
                f"Performing drag and drop by offset on element with locator type {args[0]} and locator {args[2]}"
                f"and to x-offset {x_offset} and y-offset {y_offset}")
        except Exception as e:
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])

    def check_checkbox(self, *args):
        try:
            element = self.get_element(*args)
            self.get_webdriver_wait_instance().until(ec.element_to_be_clickable(element))
            if element.is_selected():
                self.log.info(
                    f"The checkbox with locator type: {args[0]} and locator: {args[1]} is already checked")
            else:
                element.click()
                self.log.info(f"The checkbox with locator type: {args[0]} and locator: {args[1]} is checked")

        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to check the checkbox"

    def uncheck_checkbox(self, *args):
        try:
            element = self.get_element(*args)
            self.get_webdriver_wait_instance().until(ec.presence_of_element_located(element))
            if element.is_selected():
                element.click()
                self.log.info(f"Unchecking checkbox with locator type: {args[0]} and locator: {args[1]}")
            else:
                self.log.info(f"The checkbox with locator type: {args[0]} and locator: {args[1]} is unchecked")

        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to uncheck the checkbox"

    def check_multiple_checkbox(self, *args):
        try:
            elements = self.get_elements(*args)
            ele_count = len(elements)
            if ele_count > 0:
                for element in elements:
                    if element.is_selected():
                        continue
                    else:
                        element.click()
            self.log.info(f"Selecting multiple checkboxes with locator type: {args[0]} and locator: {args[1]}")
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to select multiple checkboxes"

    def uncheck_multiple_checkbox(self, *args):
        try:
            elements = self.get_elements(*args)
            ele_count = len(elements)
            if ele_count > 0:
                for element in elements:
                    if element.is_selected():
                        element.click()

            self.log.info(f"Unselecting multiple checkboxes with locator type: {args[0]} and locator: {args[1]}")
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to Unselect multiple checkboxes"

    def switch_to_frame(self, *args):
        try:
            frame_element = self.get_element(*args)
            self.get_switch_to_instance().frame(frame_element)
            self.log.info(f"Switching to the frame with locator type: {args[0]} and locator: {args[1]}")
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to switch to frame"

    def switch_to_parent_frame(self):
        try:
            self.get_switch_to_instance().parent_frame()
            self.log.info(f"Switching to the parent frame")
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to switch to the parent frame"

    def switch_to_default_content(self):
        try:
            self.get_switch_to_instance().default_content()
            self.log.info(f"Switching out of the frame")
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "unable to switch out of the frame"

    def switch_window(self, window_count):
        try:
            window_handles = self.driver.window_handles()
            self.get_switch_to_instance().window(window_handles[window_count])
            self.log.info(
                f" Switching to the window with index: {window_count} and window handler: {window_handles[window_count]}")
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, f"Unable to switch window with index: {window_count} and with window handel: {window_handles[window_count]}"

    def check_if_element_exits(self, *args):
        try:
            element = self.get_elements(*args)
            if len(element) > 0:
                self.log.info(f"The element with locator type: {args[0]} and locator: {args[1]} exits")
                return True
            else:
                self.logger.warning(f"The element with locator type: {args[0]} and locator: {args[1]} does not exits")
                return False
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "The element does not exits"

    def text_to_be_present_in_element(self, locator, text):
        try:
            self.get_webdriver_wait_instance().until(ec.text_to_be_present_in_element(locator, text))
            self.log.info(f"The text: {text} is present in locator {locator}")
            return True
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "The text was not present in the element"

    def get_attribute(self, *args, atrribute_name):
        try:
            element = self.get_element(*args)
            attribute_value = element.get_attribute(atrribute_name)
            self.log.info(f"The attribute value for attribute name :{atrribute_name} is {attribute_value}")
            return attribute_value
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to fetch attribute value"

    def get_text(self, element):
        try:

            element_text = element.text
            self.log.info(
                f"The element has a text value: {element_text}")
            return element_text
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to fetch text value"

    def get_text_element(self, *args):
        try:
            element = self.get_element(*args)
            element_text = element.text
            self.log.info(
                f"The element has a text value: {element_text}")
            return element_text
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to fetch text value"

    def get_css_properties(self, *args, property_name):
        try:
            element = self.get_element(*args)
            css_property_value = element.value_of_css_property(property_name)
            self.log.info(
                f"The css property of for element with locator type: {args[0]} and locator : {args[1]} is {css_property_value}")
            return css_property_value
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to fetch the css property value"

    def take_screenshot(self, screenshot_path):
        try:
            self.driver.save_screenshot(screenshot_path)
            self.log.info(f"The screenshot was taken successfully in location: {screenshot_path}")
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to capture screenshot"

    def take_element_screenshot(self, *args, ):
        try:
            element = self.get_element(*args)
            element.screenshot_as_png
        except Exception as e:
            print(e)
            self.log.error(e)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            assert False, "Unable to capture element screenshot"

    def waitForElement(self, *args, timeout = 10, pollFrequency = 0.5 ):
        element = None
        try:
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")

            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])

            element = wait.until(ec.element_to_be_clickable((args[0],args[1])))

            self.log.info("Element appeared on the web page")

        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
            self.log.critical(sys.exc_info()[2])
        return element

    def webScroll(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def getURL(self):
        '''
        Get the current URL
        :return: current URL
        '''
        currentURL = self.driver.current_url

        return currentURL

    def pageBack(self):
        '''
        page back the browser
        '''
        self.driver.execute_script("window.history.go(-1)")

    def getAttributeValue(self, locator="", locatorType="id", element=None, attribute=""):
        '''
        get attribute value
        '''
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            attribute_value = element.get_attribute(attribute)
        except:
            self.log.error("Failed to get " + attribute + " in element with locator: " +
                           locator + " and locatorType: " + locatorType)
            print_stack()
            self.log.critical(sys.exc_info()[2])
            attribute_value = None
        return attribute_value

    def refresh(self):
        self.driver.get(self.driver.current_url)

    def page_has_loaded(self):
        try:
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script('return document.readyState == "complete";'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script('return jQuery.active == 0'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script('return typeof jQuery != "undefined"'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script('return angular.element(document).injector().get("$http").pendingRequests.length === 0'))
        except:
            return False
