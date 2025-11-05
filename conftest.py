import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def driver(request):
    """Создаёт экземпляр браузера"""
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(20)

    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def login(request):
    """Авторизация перед выполнением тестов"""
    # ✅ получаем активный драйвер, а не None
    driver = request.getfixturevalue("driver")
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_login("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_button()
    yield
    # Можно добавить logout() при необходимости


@pytest.fixture(autouse=True)
def setup_environment_properties():
    """Создание environment.properties для Allure"""
    os.makedirs("allure-results", exist_ok=True)
    properties = {
        "STAGE": "AQA",
        "BROWSER": "Chrome"
    }
    with open("allure-results/environment.properties", "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")