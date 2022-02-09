from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import BASE_URL
from selenium.common.exceptions import WebDriverException
import time
from constants import CSS_USER_ROOT, CSS_COOKIES


class BasePage:
    """
    Base Page
    """
    url = BASE_URL
    time_to_wait = 10

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        """
        Open URL
        """
        try:
            self.driver.get(self.url)
            time.sleep(5)
            self.privacy_accept_cookies(CSS_COOKIES)
        except WebDriverException:
            print('Incorrect URL')

    def privacy_accept_cookies(self, css_selector):
        """
        Accept cookies using JS
        """
        self.wait_for_ajax()
        return self.driver.execute_script(
            f"document.querySelector('{CSS_USER_ROOT}').shadowRoot.querySelector('{css_selector}').click()"
        )

    def wait_for_ajax(self):
        """
        Wait for jQuery to be loaded and for all ajax requests to finish
        """
        return self.driver.execute_script(
            "return typeof(jQuery)!='undefined' && jQuery.active==0")

    def wait_for_css_for_single_element(self, wait_selector):
        """
        wait for css selector (wait_selector) to be present in DOM
        :param wait_selector:
        """
        return WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, wait_selector))
        )

    def wait_for_css_for_all_elements(self, wait_selector):
        """
        wait for css selector (wait_selector) to be present in DOM
        :param wait_selector:
        """
        return WebDriverWait(self.driver, self.time_to_wait).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, wait_selector))
        )

    def wait_for_visibility_of_element(self, css_selector):
        """
        Wait for css selector to be visible in DOM
        """
        return WebDriverWait(self.driver, self.time_to_wait).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, css_selector)
            )
        )
