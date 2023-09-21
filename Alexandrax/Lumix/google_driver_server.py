import argparse
import json
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class GoogleDriveAutomation:
    def __init__(self, args: argparse.Namespace):
        # Step 1: Set up the Selenium driver (you need to download the appropriate driver for your browser)
        self.__file_cache = []
        self.__settings = self.__open_settings_file()
        self.__driver_url = self.__settings.get('driver_url')

        self.__driver = webdriver.Chrome()
        # Step 2: Open Google Drive and navigate to the login page
        self.__driver.get(self.__driver_url)
        self.__parse_args(args)

        self.login_to_google_flow()  # can move from init and be called explicitly, so it can be wrapper in test as well

    def __parse_args(self, args: argparse.Namespace) -> None:
        self.__email = args.email
        self.__pwd = args.password

    def __del__(self):
        # Step 8: Close the browser window when done, using de-constructor, will run at end of this object 'life'
        self.__driver.quit()

    @property
    def settings_file(self) -> str:
        settings_file_name = 'settings.json'
        return os.path.join(os.path.dirname(__file__), settings_file_name)

    def login_to_google_flow(self) -> bool:
        try:
            self.__send_email_to_login_page()
            self.__send_pwd_to_login_page()
            # TODO: add check that actually logged in!!!! if any question for phone or other stuff
            return True
        except Exception as ex:
            print(f"Login to webpage: {self.__driver_url}, failed: {ex}")
            return False

    def get_file_list(self) -> list:
        self.__file_cache = []
        # wait till element is clickable
        element_name = 'div[role="row"]'
        self.__wait_for_element(By.CSS_SELECTOR, element_name)
        # Step 5: Retrieve a list of file elements
        file_elements = self.__get_elements_by_type(By.CSS_SELECTOR, element_name)
        self.__file_cache = file_elements
        return file_elements

    def print_total_number_of_files(self, retrieve_if_empty_cache: bool = False) -> None:
        # Step 6: Print the total number of files
        if self.__inner_file_retrieval(retrieve_if_empty_cache):
            print(f"Total number of files: {self.__file_cache}")

    def print_each_element(self, retrieve_if_empty_cache: bool = False) -> None:
        # Step 7: Loop through each file element and print their details
        if self.__inner_file_retrieval(retrieve_if_empty_cache):
            for file_element in self.__file_cache:
                filename = file_element.text
                print(f"Filename: {filename}")

    def __inner_file_retrieval(self, retrieve_if_empty_cache: bool) -> bool:
        if not self.__file_cache and retrieve_if_empty_cache:
            self.get_file_list()
        if not self.__file_cache:
            print("No files in cache, please retrieve first!")
            return False
        else:
            return True

    def __wait_for_element(self, element_type: str, element_name: str) -> None:
        time_to_wait = 30
        WebDriverWait(self.__driver, time_to_wait).until(ec.presence_of_element_located((element_type, element_name)))

    def __open_settings_file(self) -> dict:
        with open(self.settings_file, 'r') as fp:
            return json.load(fp)

    def __get_element_by_name(self, element_name: str) -> WebElement:
        element = self.__driver.find_element(By.NAME, element_name)
        return element

    def __get_elements_by_type(self, element_type: str, element_name: str) -> list[WebElement]:
        element = self.__driver.find_elements(element_type, element_name)
        return element

    @staticmethod
    def __send_keys_to_element(element: WebElement, keys: str) -> None:
        element.send_keys(keys)

    def __send_enter_to_element(self, element: WebElement) -> None:
        # Press Enter or Return key to proceed
        self.__send_keys_to_element(element, Keys.RETURN)

    def __get_email_field(self) -> WebElement:
        field_name = self.__settings.get('login')
        return self.__get_element_by_name(field_name)

    def __get_pwd_field(self) -> WebElement:
        field_name = self.__settings.get('password')
        return self.__get_element_by_name(field_name)

    def __send_email_to_login_page(self) -> None:
        # Step 3: Find and fill in the email field
        email_field = self.__get_email_field()
        self.__send_keys_to_element(email_field, self.__email)
        self.__send_enter_to_element(email_field)

    def __send_pwd_to_login_page(self) -> None:
        # Step 4: Find and fill in the password field
        self.__wait_for_element(By.NAME, self.__settings.get('password'))
        pwd_field = self.__get_pwd_field()
        self.__send_keys_to_element(pwd_field, self.__pwd)
        self.__send_enter_to_element(pwd_field)
