# login_page.py — страница авторизации (Login Page)
# Здесь описаны шаги авторизации пользователя: ввод логина, пароля и вход в систему

import allure
from base.base_page import BasePage                            # Импорт базового класса страниц
from allure_commons.types import AttachmentType                # Для прикрепления скриншотов
from data.URLs import Urls                                     # Для получения ссылки на страницу логина


class LoginPage(BasePage):                                     # Класс, описывающий страницу логина

    _PAGE_URL = Urls.LOGIN                                     # URL страницы авторизации
    _USERNAME_FILED = "//input[@id='user-name']"               # Локатор поля логина
    _PASSWORD_FILED = "//input[@id='password']"                # Локатор поля пароля
    _LOGIN_BUTTON = "//input[@id='login-button']"              # Локатор кнопки входа

    @allure.step("Ввод логина")                                # Шаг для Allure
    def enter_login(self, login):                              # Метод ввода логина
        self.driver.find_element(*self._USERNAME_FILED).send_keys(login)

    @allure.step("Ввод пароля")                                # Шаг для Allure
    def enter_password(self, password):                        # Метод ввода пароля
        self.driver.find_element(*self._PASSWORD_FILED).send_keys(password)

    @allure.step("Клик на кнопку авторизации")                 # Шаг для Allure
    def click_button(self):                                    # Метод нажатия кнопки входа
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        allure.attach(                                          # Прикрепление скриншота
            body=self.driver.get_screenshot_as_png(),
            name="Success authorization",
            attachment_type=AttachmentType.PNG
        )