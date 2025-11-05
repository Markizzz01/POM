# checkout_page.py — страница оформления заказа
# Здесь заполняются данные покупателя и осуществляется переход к следующему шагу

import allure
from base.base_page import BasePage                            # Импорт базовой страницы
from allure_commons.types import AttachmentType                # Для скриншотов
from data.URLs import Urls                                     # Для URL страницы

class CheckoutProduct(BasePage):                               # Класс страницы оформления

    _PAGE_URL = Urls.CHECKOUNT                                 # URL страницы оформления заказа
    _FIRST_NAME = "//input[@id='first-name']"                  # Поле ввода имени
    _LAST_NAME = "//input[@id='last-name']"                    # Поле ввода фамилии
    _POSTAL_CODE = "//input[@id='postal-code']"                # Поле почтового индекса
    _CONTINUE = "//input[@id='continue']"                      # Кнопка "Continue"

    @allure.step("Заполнение полей")                           # Шаг для Allure
    def enter_first(self, first):                              # Ввод имени
        self.driver.find_element(*self._FIRST_NAME).send_keys(first)

    def enter_last(self, last):                                # Ввод фамилии
        self.driver.find_element(*self._LAST_NAME).send_keys(last)

    def enter_code(self, code):                                # Ввод индекса
        self.driver.find_element(*self._POSTAL_CODE).send_keys(code)
        allure.attach(                                          # Прикрепляем скриншот после ввода данных
            body=self.driver.get_screenshot_as_png(),
            name="Registration",
            attachment_type=AttachmentType.PNG
        )

    @allure.step("Нажатие на кнопку 'Продолжить'")            # Шаг для Allure
    def enter_continue(self):                                  # Переход на следующий шаг
        self.driver.find_element(*self._CONTINUE).click()