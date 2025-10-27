# dashboard_page.py — описание страницы профиля (личного кабинета)
# Здесь находятся локаторы и методы, относящиеся к действиям на странице профиля

from base.base_page import BasePage

class DashboardPage(BasePage):

    _PAGE_URL = "https://www.freeconferencecall.com/profile/account-info-login"  # URL профиля
    _INVITE_BUTTON = "//button[@title='Пригласить']"  # Локатор кнопки "Пригласить"

    def click_invite_button(self):
        self.driver.find_element(*self._INVITE_BUTTON).click()  # Нажимаем кнопку "Пригласить"