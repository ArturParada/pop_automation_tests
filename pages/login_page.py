from selenium.webdriver.support.wait import WebDriverWait

from pages.base_pages import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators


class LoginPage(BasePage):

    def click_register_btn(self):

        wait = WebDriverWait(self.driver, 60)
        element = wait.until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_BTN))
        element.click()