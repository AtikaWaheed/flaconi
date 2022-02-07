"""
Flaconi Home Page Tests
"""
import unittest
from selenium import webdriver


class BaseTests(unittest.TestCase):
    """
    Base Test Class
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        """
        Tear down
        """
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
