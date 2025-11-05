import pytest
import allure
from base.base_test import BaseTest

@allure.epic("Swag Labs")                                                 # Epic Allure
@allure.feature("Авторизация")                                           # Feature Allure
@pytest.mark.usefixtures("driver")                                       # Фикстура браузера
class TestLogin(BaseTest):                                                # Тест логина
    @allure.title("Успешный вход пользователя")                           # Заголовок теста
    def test_login(self):
        self.login_page.open()                                            # Открываем страницу логина
        self.login_page.enter_login(self.data.LOGIN)                      # Вводим логин
        self.login_page.enter_password(self.data.PASSWORD)               # Вводим пароль
        self.login_page.click_button()                                    # Кликаем "Login"

@allure.epic("Swag Labs")
@allure.feature("Добавление товаров и проверка корзины")
@pytest.mark.usefixtures("driver", "login")                               # Фикстура авторизации
class TestCartFlow(BaseTest):                                             # Тест корзины
    @allure.title("Добавление товаров в корзину и проверка корзины")
    def test_add_products_and_check_cart(self):
        self.products_page.open()                                         # Открываем страницу товаров
        self.products_page.add_product_one()                               # Добавляем рюкзак
        self.products_page.add_product_two()                               # Добавляем фонарь
        self.products_page.add_product_three()                             # Добавляем футболку
        self.cart_page.open()                                              # Открываем корзину
        self.cart_page.checking_cart()                                     # Проверяем заголовок корзины
        self.cart_page.check_all_items_in_cart()                           # Проверяем все товары
        self.cart_page.checkout_enter()                                    # Переходим к оформлению заказа

@allure.epic("Swag Labs")
@allure.feature("Оформление заказа")
@pytest.mark.usefixtures("driver", "login")
class TestCheckout(BaseTest):                                             # Тест оформления заказа
    @allure.title("Заполнение формы оформления заказа")
    def test_checkout(self):
        self.checkout_page.open()                                         # Открываем страницу оформления
        self.checkout_page.enter_first("Alexey")                           # Вводим имя
        self.checkout_page.enter_last("Egorushkov")                        # Вводим фамилию
        self.checkout_page.enter_code("123456")                             # Вводим почтовый индекс
        self.checkout_page.enter_continue()                                 # Кликаем "Continue"

@allure.epic("Swag Labs")
@allure.feature("Завершение покупки")
@pytest.mark.usefixtures("driver", "login")
class TestFinish(BaseTest):                                               # Тест завершения покупки
    @allure.title("Завершение покупки и возврат на главную страницу")
    def test_finish(self):
        self.finish_page.open()                                           # Открываем страницу завершения
        self.finish_page.complete_page()                                   # Проверяем заголовок "Checkout: Complete!"
        self.finish_page.home_page()                                        # Возврат на главную страницу