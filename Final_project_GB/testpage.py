import logging
from BaseApp import BasePage
import requests
from requests.exceptions import HTTPError
from selenium.webdriver.common.by import By
import yaml


class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = By.XPATH, locators["xpath"][locator]
    for locator in locators["css"].keys():
        ids[locator] = By.CSS_SELECTOR, locators["css"][locator]


class OperationsHelper(BasePage):

    # enter text into field
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send '{word}' to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operate with {locator}")
            return False
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=2)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We found text {text} in field {element_name}")
        return text

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f"Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_css_property(self, locator, property_name, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        element = self.find_element(locator, time=2)
        if not element:
            return None
        try:
            css_property = element.value_of_css_property(property_name)
            logging.debug(f"CSS property '{property_name}' of element {element_name}: {css_property}")
            return css_property
        except:
            logging.exception(f"Exception while getting CSS property '{property_name}' of element {element_name}")
            return None

    # enter smth into fields
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")

    # click to buttons

    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")

    def click_about(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_ABOUT"], description="click ABOUT")

    # get smth from object
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="Error label")

    def get_username_label(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_POSITIVE_ENTER"], description="Success login")

    def get_about_header(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ABOUT_HEADER"], description="Success about")

    def get_about_css_property(self):
        return self.get_css_property(TestSearchLocators.ids["LOCATOR_ABOUT_HEADER"], 'font-size',
                                     description="Font size is correct")
