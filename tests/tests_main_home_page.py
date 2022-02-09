from tests.test_base import TestsBase
from pages.main_home_page import HomePage
from constants import HOME_PAGE_TITLE, CSS_COOKIES


class FlaconiHomePageTests(TestsBase):
    """
    This class contains all Landing Page test functions
    """

    def setUp(self):
        super(FlaconiHomePageTests, self).setUp()
        self.home_page = HomePage(self.driver)

    def test_is_browser_on_page(self):
        """
        Make sure correct page is open
        verify Page title is correct
        """
        self.home_page.visit()
        self.assertEqual(self.home_page.is_browser_on_page(), HOME_PAGE_TITLE)

    def test_nav_makeup_sublinks_are_valid_and_return_200_status_code(self):
        """
        1- Visit page and accept cookies
        2- Hover over makeup option and validate status code for all sublinks
        """
        self.home_page.visit()
        self.assertTrue(self.home_page.hover_over_main_nav_option_and_verify_all_sublinks(4))
