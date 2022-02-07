"""
Flaconi Product Details Page which is ready to be added in cart
"""
from pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    """
    This class contains all functions on Flaconi Product Details Page
    """
    def is_browser_on_page(self):
        """
        check browser is on home page
        """
        return self.wait_for_visibility_of_element("[class*='ProductInformationContainerstyle__Headline']")

    def get_selected_product_type(self):
        """
        Get the brand name of selected product
        """
        product_name = self.wait_for_css_for_single_element("div [class*='BrandProductNameAndTypestyle__Wrapper'] a")
        product_title = product_name.get_attribute('title')
        return product_title

    def get_add_to_cart_button(self):
        """
        Get element of Add to cart button
        """
        return self.wait_for_css_for_single_element("button[class*='PDPActionBarstyle__Button'] ")

    def get_added_product_from_modal(self):
        """
        Make sure product is added
        """
        return self.wait_for_visibility_of_element("div[class*='AddedProductInfostyle__Wrapper'] ")

    def get_go_to_the_cart_button(self):
        """
        Get the 'Zum Warenkorb' button
        """
        return self.wait_for_css_for_single_element("div[class*='AddedToCartFooterstyle__Wrapper'] a")
