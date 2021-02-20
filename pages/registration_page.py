from pages.base_pages import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators import RegistrationPageLocators


class RegistrationPage(BasePage):

    def _verify_page(self):
        print("Weryfikacja RegistartionPage")
        # Tutaj będziemy weryfikować stronę
        wait = WebDriverWait(self.driver, 60)
        # Wywołanie metody until na obiekcie WebDriverWait
        # W efekcie otrzymamy element (jeśli warunek wystąpi)
        wait.until(EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT))

    def fill_name(self,name):
        element = self.driver.find_element(*RegistrationPageLocators.NAME_INPUT)
        element.send_keys(name)

    def fill_surname(self,surname):
        element = self.driver.find_element(*RegistrationPageLocators.SURNAME_INPUT)
        element.send_keys(surname)

    def fill_email(self, email):
        element = self.driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        element.send_keys(email)

    def fill_password(self,password):
        element = self.driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        element.send_keys(password)

    def fill_rp_password(self,rp_password):
        element = self.driver.find_element(*RegistrationPageLocators.PASSWORD_RP_INPUT)
        element.send_keys(rp_password)

    def fill_adreess(self,adreess):
        element = self.driver.find_element(*RegistrationPageLocators.ADREESS_INPUT)
        element.send_keys(adreess,Keys.RETURN)