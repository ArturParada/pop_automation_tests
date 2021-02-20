from pages.base_pages import BasePage
from locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):

    def click_zaloguj_btn(self):
        wait = WebDriverWait(self.driver, 60)
        element = wait.until(EC.element_to_be_clickable(HomePageLocators.ZALOGUJ_BTN))
        element.click()

    def click_cookies_accept(self):
        wait = WebDriverWait(self.driver, 60)
        element = wait.until(EC.element_to_be_clickable(HomePageLocators.COOKIES_ACCEPT))
        element.click()

    def _verify_page(self):
        assert "ZARA Polska / Poland | Nowa Kolekcja Online" in self.driver.title
