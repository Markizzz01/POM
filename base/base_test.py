# base_test.py — базовый класс для всех тестов
# Здесь создаются объекты всех страниц, чтобы их можно было использовать в тестах

from pages.login_page import LoginPage                     # Импорт страницы авторизации
from pages.products_page import ProductPage                 # Импорт страницы с товарами
from pages.cart_page import CartPage                        # Импорт страницы корзины
from pages.checkout_page import CheckoutProduct             # Импорт страницы оформления заказа
from pages.finish_page import FinishRegistration            # Импорт страницы завершения покупки
from data.credentials import Credentials                    # Импорт данных для авторизации

class BaseTest:                                             # Базовый класс для всех тестов
    def setup_method(self):                                 # Метод, выполняющийся перед каждым тестом
        self.login_page = LoginPage(self.driver)            # Создание объекта страницы авторизации
        self.products_page = ProductPage(self.driver)       # Создание объекта страницы с товарами
        self.cart_page = CartPage(self.driver)              # Создание объекта страницы корзины
        self.checkout_page = CheckoutProduct(self.driver)   # Создание объекта страницы оформления
        self.finish_page = FinishRegistration(self.driver)  # Создание объекта страницы завершения покупки
        self.data = Credentials()                           # Подключаем класс с логином и паролем