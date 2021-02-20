import unittest
from selenium import webdriver
from time import sleep

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.zara.com/pl/")
        self.driver.maximize_window()

    def tearDown(self):
        sleep(20)

        self.driver.quit()