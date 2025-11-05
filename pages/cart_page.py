# cart_page.py — страница корзины
# Здесь выполняется проверка содержимого корзины и переход к оформлению заказа

import allure
from base.base_page import BasePage                            # Импорт базового класса
from allure_commons.types import AttachmentType                # Для скриншотов
from data.URLs import Urls                                     # Для URL страницы

class CartPage(BasePage):                                      # Класс страницы корзины

    _PAGE_URL = Urls.CART                                      # URL корзины
    _CHECKING_CART = "//span[@class='title']"                  # Заголовок страницы корзины
    _BACKPACK_ITEM = "//div[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']"   # Товар 1
    _BIKE_LIGHT_ITEM = "//div[@data-test='inventory-item-name' and text()='Sauce Labs Bike Light']" # Товар 2
    _BOLT_SHIRT_ITEM = "//div[@data-test='inventory-item-name' and text()='Sauce Labs Bolt T-Shirt']" # Товар 3
    _CHECKOUT = "//button[@id='checkout']"                     # Кнопка оформления заказа

    @allure.step("Переход в корзину")                          # Шаг для Allure
    def checking_cart(self):                                   # Проверяем, что открыта страница корзины
        element = self.driver.find_element(*self._CHECKING_CART)
        assert element.text == "Your Cart"
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Cart page",
            attachment_type=AttachmentType.PNG
        )

    @allure.step("Проверка добавленных товаров")               # Шаг для Allure
    def check_all_items_in_cart(self):                         # Проверяем, что товары в корзине
        assert self.driver.find_element(*self._BACKPACK_ITEM).is_displayed(), "Backpack нет в корзине"
        assert self.driver.find_element(*self._BIKE_LIGHT_ITEM).is_displayed(), "Bike Light нет в корзине"
        assert self.driver.find_element(*self._BOLT_SHIRT_ITEM).is_displayed(), "Bolt T-Shirt нет в корзине"

    def checkout_enter(self):                                  # Клик по кнопке Checkout
        self.driver.find_element(*self._CHECKOUT).click()