from selenium.webdriver.common.by import By

class HomePageLocators:

    ZALOGUJ_BTN = (By.LINK_TEXT, 'LOGOWANIE')
    COOKIES_ACCEPT = (By.ID,'onetrust-accept-btn-handler')


class LoginPageLocators:
    REGISTER_BTN = (By.XPATH, '//button[@class="button logon-view__alternate-section-button"]')

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, '//input[@name="firstName"]')
    SURNAME_INPUT = (By.XPATH,'//input[@name="lastName"]')