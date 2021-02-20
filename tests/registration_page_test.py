import unittest

from pages.login_page import LoginPage
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from time import sleep



valid_name = "Artur"
valid_surname = "Kowalski"

class RegistrationPageTest(BaseTest):


    def setUp(self):
        super().setUp()
        hp = HomePage(self.driver)
        hp.click_cookies_accept()
        hp.click_zaloguj_btn()
        lp = LoginPage(self.driver)
        lp.click_register_btn()

    def incorrect_name(self):
        rp = RegistrationPage(self.driver)
        rp.fill_name(valid_name)



    sleep(3)


if __name__=="__main__":
    unittest.main(verbosity=2)