import unittest

from pages.login_page import LoginPage
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from time import sleep



valid_name = "Artur"
valid_surname = "Kowalski"
valid_email= 'asdasasdfsdfas@onet.pl'
valid_password = "sadasdasd"
valid_rp_password = valid_password
valid_adreess = "Wiejska "
valid_phone_number = "123456"
valid_zip_code = '90-333'
valid_town = 'Łódź'
valid_province = 'ŁÓDZKIE'

class RegistrationPageTest(BaseTest):


    def setUp(self):
        super().setUp()
        hp = HomePage(self.driver)
        hp.click_cookies_accept()
        hp.click_zaloguj_btn()
        lp = LoginPage(self.driver)
        lp.click_register_btn()

    def test_incorrect_name(self):
        rp = RegistrationPage(self.driver)
        rp.fill_name(valid_name)
        rp.fill_surname(valid_surname)
        rp.fill_email(valid_email)
        rp.fill_password(valid_password)
        rp.fill_rp_password(valid_rp_password)
        rp.fill_adreess(valid_adreess)
        rp.phone_number(valid_phone_number)
        rp.zip_code(valid_zip_code)
        rp.town_name(valid_town)
        rp.choose_province(valid_province)
        rp.click_zl()




    sleep(3)


if __name__=="__main__":
    unittest.main(verbosity=2)