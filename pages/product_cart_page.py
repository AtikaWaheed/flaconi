"""
Flaconi Shopping Cart Page
"""
from pages.base_page import BasePage


class ShoppingCartPage(BasePage):
    """
    This class contains all functions on Flaconi Shopping Cart Page
    """
    def is_browser_on_page(self):
        """
        check browser is on home page
        """
        return self.wait_for_visibility_of_element("div [class*='CartSummarystyle__Wrapper']")

    def enter_code_in_voucher_code_field_and_submit(self, enter_code):
        """
        Enter voucher code field on Cart page and submit
        """
        self.wait_for_css_for_single_element("#voucherCode").send_keys(enter_code)
        self.wait_for_css_for_single_element("[class*='VoucherFormstyle__ButtonWrapper'] button").click()

    def get_the_error_by_entering_wrong_voucher_code(self):
        """
        Note the error message appeared
        """
        return self.wait_for_css_for_single_element("div [class*='NotificationInlinestyle__Message']").text
