from selenium.webdriver.support.select import Select

from pages.base_pages import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators import RegistrationPageLocators



class RegistrationPage(BasePage):

    def _verify_page(self):
        print("Weryfikacja RegistartionPage")

        wait = WebDriverWait(self.driver, 60)
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
        element.send_keys(adreess)


    def phone_number(self,phone_number):
        element = self.driver.find_element(*RegistrationPageLocators.PHONE)
        element.send_keys(phone_number)

    def zip_code (self,zip_code):
        element = self.driver.find_element(*RegistrationPageLocators.ZIP_CODE_INPUT)
        element.send_keys(zip_code)

    def town_name(self,town):
        element = self.driver.find_element(*RegistrationPageLocators.TOWN_INPUT)
        element.send_keys(town)

    def choose_province(self,province):

        self.driver.find_element(*RegistrationPageLocators.PROVINCE_INPUT).click()
        province_options=self.driver.find_element(*RegistrationPageLocators.PROVINCE_INPUT)

        for option in province_options.find_elements_by_tag_name('option'):
            if option.get_attribute("innerText")== province:
                option.click()
                break

    def verify_visible_errors(self,error_texts):
        pass



    def click_zl(self):
        self.driver.find_element(*RegistrationPageLocators.ZL_BUTTON).click()
