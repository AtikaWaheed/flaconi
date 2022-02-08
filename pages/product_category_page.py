"""
Flaconi Product Category Page
"""
import random
from pages.base_page import BasePage
from constants import CSS_PROD_TITLE, CSS_FOR_ALL_PROD_ITEMS


class ProductsCategoryPage(BasePage):
    """
    This class contains all functions on Flaconi Product Category Page
    """
    def get_product_page_header_title_text(self):
        """
        Get the header text for main title
        Convert into Upper case
        """
        uppercase_header_text = self.wait_for_css_for_single_element(CSS_PROD_TITLE).text
        return uppercase_header_text.upper()

    def choose_random_product_from_category(self):
        """
        Get all products, and random select any
        Get selected product 'Brand Name text' before click.
        """
        product_type = self.wait_for_css_for_all_elements(CSS_FOR_ALL_PROD_ITEMS)
        random_product_name = random.choice(product_type)
        product_brand_text = random_product_name.text
        random_product_name.click()
        return product_brand_text
