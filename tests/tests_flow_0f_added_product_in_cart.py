from tests.base_test import BaseTests
from pages.main_home_page import HomePage
from pages.product_category_page import ProductsCategoryPage
from pages.product_details_page import ProductDetailsPage
from pages.product_cart_page import ShoppingCartPage
from constants import WRONG_VOUCHER_CODE, CSS_COOKIES
import time


class FlaoniProductCategoryTests(BaseTests):
    """
    This class contains all Landing Page test functions
    """

    def setUp(self):
        super(FlaoniProductCategoryTests, self).setUp()
        self.home_page = HomePage(self.driver)
        self.product_category_page = ProductsCategoryPage(self.driver)
        self.product_details_page = ProductDetailsPage(self.driver)
        self.shopping_cart_page = ShoppingCartPage(self.driver)

    def test_flow_of_adding_product_in_the_cart_and_validate_error_msg_on_wrong_voucher(self):
        """
        1- Move to home page
        2- Accept cookies
        3- Click on home page navigation option (parfum), Assert title header text with clicked option.
        4- Click random product on category page.
        5- Validate product brand header text on details page.
        """
        self.home_page.visit()
        self.home_page.privacy_accept_cookies(CSS_COOKIES)
        clicked_product_text = self.home_page.click_any_main_nav_option()
        self.assertEqual(self.product_category_page.get_product_page_header_title_text(), clicked_product_text)

        selected_product_brand_name = self.product_category_page.choose_random_product_from_category()
        self.assertEqual(self.product_details_page.get_selected_product_type(), selected_product_brand_name)
        # from nose.tools import set_trace;set_trace()

        # Click on ADD to cart button
        self.product_details_page.get_add_to_cart_button().click()

        # Product is added in cart
        self.assertTrue(self.product_details_page.get_added_product_from_modal())

        # Click on 'Zum Warenkorb' button and make sure cart page is opened
        self.product_details_page.get_go_to_the_cart_button().click()
        self.assertTrue(self.shopping_cart_page.is_browser_on_page())

        # Enter wrong Voucher and click submit button
        self.shopping_cart_page.enter_code_in_voucher_code_field_and_submit(WRONG_VOUCHER_CODE)
        self.assertEqual(self.shopping_cart_page.get_the_error_by_entering_wrong_voucher_code(),
                         WRONG_VOUCHER_CODE)






