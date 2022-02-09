"""
Flaconi Home Page Tests
"""
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class TestsBase(unittest.TestCase):
    """
    Base Test Class
    """
    opts = Options()
    opts.log.level = 'trace'

    def setUp(self):
        """ can uncomment/comment browsers on the base of requirement"""
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def tearDown(self):
        """
        Tear down
        """
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
