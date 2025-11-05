# products_page.py — страница списка товаров
# Здесь выполняются шаги по добавлению товаров в корзину

import allure
from base.base_page import BasePage                            # Импорт базовой страницы
from allure_commons.types import AttachmentType                # Для прикрепления скриншотов
from data.URLs import Urls                                     # Для получения ссылки на страницу

class ProductPage(BasePage):                                   # Класс для страницы с товарами

    _PAGE_URL = Urls.PRODUCT                                   # URL страницы товаров
    _PRODUCT_ONE = "//button[@id='add-to-cart-sauce-labs-backpack']"    # Кнопка добавления рюкзака
    _PRODUCT_TWO = "//button[@id='add-to-cart-sauce-labs-bike-light']"  # Кнопка добавления фонаря
    _PRODUCT_THREE = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"  # Кнопка добавления футболки

    @allure.step("Добавление 1 товара")                        # Шаг для Allure
    def add_product_one(self):                                 # Добавление первого товара
        self.driver.find_element(*self._PRODUCT_ONE).click()

    @allure.step("Добавление 2 товара")                        # Шаг для Allure
    def add_product_two(self):                                 # Добавление второго товара
        self.driver.find_element(*self._PRODUCT_TWO).click()

    @allure.step("Добавление 3 товара")                        # Шаг для Allure
    def add_product_three(self):                               # Добавление третьего товара
        self.driver.find_element(*self._PRODUCT_THREE).click()
        cart_count = self.driver.find_element("class name", "shopping_cart_badge")  # Проверка счетчика корзины
        assert cart_count.text == "3"                          # Проверяем, что добавлены все 3 товара
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Success add product",
            attachment_type=AttachmentType.PNG
        )