"""
Flaconi Shopping Cart Page
"""
from pages.base_page import BasePage
from constants import (
    CSS_CART_STYLE,
    CSS_VOUCHER_CODE_FIELD,
    CSS_VOUCHER_CODE_SUBMIT_BUTTON,
    CSS_ERR_WRONG_CODE
)


class ShoppingCartPage(BasePage):
    """
    This class contains all functions on Flaconi Shopping Cart Page
    """
    def is_browser_on_page(self):
        """
        check browser is on home page
        """
        return self.wait_for_visibility_of_element(CSS_CART_STYLE)

    def enter_code_in_voucher_code_field_and_submit(self, enter_code):
        """
        Enter voucher code field on Cart page and submit
        """
        self.wait_for_css_for_single_element(CSS_VOUCHER_CODE_FIELD).send_keys(enter_code)
        self.wait_for_css_for_single_element(CSS_VOUCHER_CODE_SUBMIT_BUTTON).click()

    def get_the_error_by_entering_wrong_voucher_code(self):
        """
        Note the error message appeared
        """
        return self.wait_for_css_for_single_element(CSS_ERR_WRONG_CODE).text
