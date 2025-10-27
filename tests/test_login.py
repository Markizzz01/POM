# test_login.py — тест на авторизацию пользователя
# Использует POM: LoginPage и DashboardPage через BaseTest

import pytest
import time
from base.base_test import BaseTest

@pytest.mark.usefixtures("driver")  # Подключаем фикстуру driver (из conftest.py)
class TestLogin(BaseTest):

    def test_login(self):
        self.login_page.open()  # 1. Открываем страницу логина
        self.login_page.enter_login("qwerty12@mail.ru")  # 2. Вводим логин
        self.login_page.enter_password("qwerty123")  # 3. Вводим пароль
        self.login_page.click_submit_button()  # 4. Кликаем кнопку "Войти"
        self.dashboard_page.click_invite_button()  # 5. Нажимаем "Пригласить" на странице профиля
        time.sleep(5)  # 6. Ждём для наглядности