# login_page.py — описание страницы логина
# Здесь находятся локаторы и методы для действий на странице входа

from base.base_page import BasePage

class LoginPage(BasePage):

    _PAGE_URL = "https://www.freeconferencecall.com/ru/ru/login"  # URL страницы логина

    # Локаторы страницы
    _LOGIN_FILED = "//input[@id='login_email']"
    _PASSWORD_FELID = "//input[@id='password']"
    _SUBMIT_BUTTON = "//button[@id='loginformsubmit']"

    # Методы для взаимодействия
    def enter_login(self, login):
        self.driver.find_element(*self._LOGIN_FILED).send_keys(login)  # Вводим логин

    def enter_password(self, password):
        self.driver.find_element(*self._PASSWORD_FELID).send_keys(password)  # Вводим пароль

    def click_submit_button(self):
        self.driver.find_element(*self._SUBMIT_BUTTON).click()  # Кликаем кнопку входа