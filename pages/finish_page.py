# finish_page.py — страница завершения покупки
# Здесь выполняется проверка успешного завершения покупки и возврат на главную страницу

import allure
from base.base_page import BasePage                            # Импорт базового класса
from allure_commons.types import AttachmentType                # Для скриншотов
from data.URLs import Urls                                     # Для URL страницы

class FinishRegistration(BasePage):                            # Класс страницы завершения покупки

    _PAGE_URL = Urls.FINISH                                    # URL страницы завершения
    _COMPLETE_TITLE = "//span[@data-test='title' and text()='Checkout: Complete!']"  # Заголовок
    _HOME_BUTTON = "//button[@id='back-to-products']"          # Кнопка возврата на главную

    @allure.step("Страница завершения покупки")                # Шаг для Allure
    def complete_page(self):                                   # Проверяем, что покупка завершена
        element = self.driver.find_element(*self._COMPLETE_TITLE)
        assert element.text == "Checkout: Complete!"
        allure.attach(                                          # Прикрепляем скриншот
            body=self.driver.get_screenshot_as_png(),
            name="Finish product",
            attachment_type=AttachmentType.PNG
        )

    @allure.step("Возврат на главную страницу")                # Шаг для Allure
    def home_page(self):                                       # Клик по кнопке возврата
        self.driver.find_element(*self._HOME_BUTTON).click()
        allure.attach(                                          # Прикрепляем скриншот
            body=self.driver.get_screenshot_as_png(),
            name="Home page",
            attachment_type=AttachmentType.PNG
        )