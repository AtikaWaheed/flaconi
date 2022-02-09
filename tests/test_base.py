"""
Flaconi Home Page Tests
"""
import unittest
from selenium import webdriver


class TestsBase(unittest.TestCase):
    """
    Base Test Class
    """

    def setUp(self):
        """
        can uncomment/comment browsers on the base of requirement
        """
        self.driver = webdriver.Chrome(executable_path=r'../drivers/chromedriver')
        # self.driver = webdriver.Firefox(executable_path=r'../drivers/geckodriver')
        self.driver.maximize_window()

    def tearDown(self):
        """
        Tear down
        """
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
