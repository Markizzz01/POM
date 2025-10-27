# base_page.py — базовый класс для всех страниц (POM)
# Здесь описывается логика, общая для всех страниц: открытие, локаторы, общие действия

from selenium.webdriver.remote.webdriver import WebDriver
from metaclasses.meta_locator import MetaLocator  # Мета-класс, который сам преобразует локаторы в кортежи

class BasePage(metaclass=MetaLocator):
    _LOGO = "//a[contains(@class, 'navbar-brand')]"  # Пример общего локатора, доступного на всех страницах

    def __init__(self, driver):
        self.driver: WebDriver = driver  # Сохраняем драйвер, чтобы работать с браузером

    def open(self):
        self.driver.get(self._PAGE_URL)  # Метод открытия страницы по URL