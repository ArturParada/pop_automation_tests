import unittest
from tests.base_test import BaseTest
from pages.home_page import HomePage
#from pages.login_page import LoginPage
#from pages.registration_page import RegistrationPage
from time import sleep





class RegistrationPageTest(BaseTest):


    def setUp(self):
        super().setUp()
        hp = HomePage(self.driver)
        hp.click_cookies_accept()
        hp.click_zaloguj_btn()

    def test(self):
        pass



    sleep(3)


if __name__=="__main__":
    unittest.main(verbosity=2)