"""
Flaconi Main Home Page
"""
import requests
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import time
from constants import (
    BASE_URL,
    CSS_FOR_NAV_OPTIONS,
    CSS_FOOTER
)


class HomePage(BasePage):
    """
    This class contains all functions on Flaconi Home Page
    """

    def is_browser_on_page(self):
        """
        check browser is on home page
        """
        page_title = self.driver.title
        self.wait_for_visibility_of_element(CSS_FOOTER)
        return page_title

    def get_main_nav_option(self, main_nav_option_count):
        """
        Get {required} element from main navigation
        """
        return self.wait_for_css_for_single_element(f'{CSS_FOR_NAV_OPTIONS}:nth-child({main_nav_option_count})')

    def hover_over_main_nav_option_and_verify_all_sublinks(self, main_nav_option_count):
        """
        1- Perform Hover action on {required} option
        2- Get all sublinks under Makeup Nav option.
        3- Get source code of all sublinks.
        PS: This is a generic function, which will help to extract all sub links from all main nav options
        """
        a = ActionChains(self.driver)
        nav_makeup_option = self.get_main_nav_option(main_nav_option_count)
        a.move_to_element(nav_makeup_option).perform()

        href_elems = self.wait_for_css_for_all_elements(
            f"{CSS_FOR_NAV_OPTIONS}:nth-child({main_nav_option_count}) > ul > li [href]")

        for each_elem in href_elems:
            href_request = requests.head(each_elem.get_attribute('href'))
            if href_request.status_code != 200:
                return False
        return True

    def click_any_main_nav_option(self):
        """
        CLick on option that needs to check
        :return: product option text
        """
        product_option_to_be_clicked = self.get_main_nav_option(2)
        product_text = product_option_to_be_clicked.text
        product_option_to_be_clicked.click()
        time.sleep(3)
        return product_text
