# base_test.py — базовый класс для всех тестов
# Здесь создаются объекты всех страниц, чтобы их можно было использовать в тестах

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

class BaseTest:
    def setup_method(self):
        self.login_page = LoginPage(self.driver)  # Объект страницы логина
        self.dashboard_page = DashboardPage(self.driver)  # Объект страницы профиля