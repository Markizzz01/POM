# base_page.py — базовый класс для всех страниц (POM)
# Здесь описывается логика, общая для всех страниц: открытие, локаторы, общие действия

from selenium.webdriver.remote.webdriver import WebDriver      # Импорт класса WebDriver для аннотации типов
from metaclasses.meta_locator import MetaLocator                # Подключаем метакласс, который превращает строки локаторов в кортежи


class BasePage(metaclass=MetaLocator):                          # Базовый класс для всех страниц, использует метакласс
    _LOGO = "//div[@class='app_logo']"                          # Пример общего локатора (лого сайта)

    def __init__(self, driver):                                 # Конструктор принимает объект драйвера
        self.driver: WebDriver = driver                         # Сохраняем драйвер как атрибут экземпляра

    def open(self):                                             # Метод для открытия страницы
        self.driver.get(self._PAGE_URL)                         # Переход по URL страницы