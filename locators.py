from selenium.webdriver.common.by import By

class HomePageLocators:

    ZALOGUJ_BTN = (By.LINK_TEXT, 'LOGOWANIE')
    COOKIES_ACCEPT = (By.ID,'onetrust-accept-btn-handler')


class LoginPageLocators:
    REGISTER_BTN = (By.XPATH, '//button[@class="button logon-view__alternate-section-button"]')

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, '//input[@name="firstName"]')
    SURNAME_INPUT = (By.XPATH,'//input[@name="lastName"]')
    EMAIL_INPUT = (By.XPATH, '//input[@name="email"]')
    PASSWORD_RP_INPUT = (By.XPATH,  '//input[@name="passwordConfirm"]')
    PASSWORD_INPUT = (By.XPATH,  '//input[@name="password"]')
    ADREESS_INPUT = (By.ID,'downshift-0-input')
    PHONE = (By.XPATH, '//input[@name="phones[0].subscriberNumber"]')
    ZIP_CODE_INPUT = (By.XPATH,'//input[@name="zipCode"]')
    TOWN_INPUT = (By.XPATH, '//input[@name="city"]')
    PROVINCE_INPUT = (By.XPATH, '//select[@name="stateCode"]')
    PROVINCE_OPTION = (By.XPATH, '//select[@name="stateCode"]/option')
    ERROR_MESSAGES = (By.XPATH, '//div[@class="form-input__error"]/text()')
    ZL_BUTTON = (By.XPATH,'//button[@class="button"]')

