import unittest
import pytest
import allure

from pages.login_page import LoginPage
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from time import sleep
import csv
from ddt import ddt, data, unpack



valid_name = "Artur"
valid_surname = "Kowalski"
valid_email= 'asdasasdfsdfas@onet.pl'
valid_password = "Artur12345@"
valid_rp_password = "Artur12345@"
valid_adreess = "Wiejska "
valid_phone_number = "123456"
valid_zip_code = '90-333'
valid_town = 'Łódź'
valid_province = 'ŁÓDZKIE'

def get_data(file_name):
    rows = []
    data_file = open(file_name, 'rt')
    reader = csv.reader(data_file)
    # Pomijam pierwszy wiersz
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows
@ddt
class RegistrationPageTest(BaseTest):


    def setUp(self):
        super().setUp()
        hp = HomePage(self.driver)
        hp.click_cookies_accept()
        hp.click_zaloguj_btn()
        lp = LoginPage(self.driver)
        lp.click_register_btn()

    @data(*get_data("ddt_date.csv"))
    @unpack
    @allure.testcase("without_email_phone_number_adreess")
    def test_without_email_phone_number_adreess(self, name,surname,pasword,rp_password,zip_cod,town,province ):
        rp = RegistrationPage(self.driver)
        rp.fill_name(name)
        rp.fill_surname(surname)
        rp.fill_password(pasword)
        rp.fill_rp_password(rp_password)
        rp.zip_code(zip_cod)
        rp.town_name(town)
        rp.choose_province(province)
        rp.click_zl()
        rp.verify_visible_errors(3, ["To pole jest obowiązkowe.","To pole jest obowiązkowe.","To pole jest obowiązkowe.",])


    @allure.testcase("without_phone_number")
    def test_without_phone_number(self):
        rp = RegistrationPage(self.driver)
        rp.fill_name(valid_name)
        rp.fill_surname(valid_surname)
        rp.fill_email(valid_email)
        rp.fill_password(valid_password)
        rp.fill_rp_password(valid_rp_password)
        rp.fill_adreess(valid_adreess)
        #rp.phone_number(valid_phone_number)
        rp.zip_code(valid_zip_code)
        rp.town_name(valid_town)
        rp.choose_province(valid_province)
        rp.click_zl()
        rp.verify_visible_errors(1,["To pole jest obowiązkowe."])


    @allure.testcase("test_without_email")
    def test_without_email(self):
        rp = RegistrationPage(self.driver)
        rp.fill_name(valid_name)
        rp.fill_surname(valid_surname)
        #rp.fill_email(valid_email)
        rp.fill_password(valid_password)
        rp.fill_rp_password(valid_rp_password)
        rp.fill_adreess(valid_adreess)
        rp.phone_number(valid_phone_number)
        rp.zip_code(valid_zip_code)
        rp.town_name(valid_town)
        rp.choose_province(valid_province)
        rp.click_zl()
        rp.verify_visible_errors(1, ["To pole jest obowiązkowe."])


    @allure.testcase("without_password")
    def test_without_password(self):
        rp = RegistrationPage(self.driver)
        rp.fill_name(valid_name)
        rp.fill_surname(valid_surname)
        rp.fill_email(valid_email)
        #rp.fill_password(valid_password)
        rp.fill_rp_password(valid_rp_password)
        rp.fill_adreess(valid_adreess)
        rp.phone_number(valid_phone_number)
        rp.zip_code(valid_zip_code)
        rp.town_name(valid_town)
        rp.choose_province(valid_province)
        rp.click_zl()
        rp.verify_visible_errors(1,["To pole jest obowiązkowe."])


    @allure.testcase("without_password_and_rppassword")
    def test_without_password_and_rppassword(self):
        rp = RegistrationPage(self.driver)
        rp.fill_name(valid_name)
        rp.fill_surname(valid_surname)
        rp.fill_email(valid_email)
        # rp.fill_password(valid_password)
        #rp.fill_rp_password(valid_rp_password)
        rp.fill_adreess(valid_adreess)
        rp.phone_number(valid_phone_number)
        rp.zip_code(valid_zip_code)
        rp.town_name(valid_town)
        rp.choose_province(valid_province)
        rp.click_zl()
        rp.verify_visible_errors(2, ["To pole jest obowiązkowe.","To pole jest obowiązkowe."])





    sleep(3)


if __name__=="__main__":
    unittest.main(verbosity=2)