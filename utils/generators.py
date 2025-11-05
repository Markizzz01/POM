
# Вспомогательная библиотека для генерации случайных тестовых данных
# Используется для подставления данных в тестах (логины, пароли, номера и т.д.)

import random
import string
from faker import Faker

fake = Faker()  # Используем библиотеку Faker для более реалистичных данных

class Generators:
    """Класс для генерации случайных данных"""

    @staticmethod
    def generate_string(length=10):
        """Генерирует случайную строку заданной длины"""
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    @staticmethod
    def generate_number(min_val=0, max_val=100):
        """Генерирует случайное число в заданном диапазоне"""
        return random.randint(min_val, max_val)

    @staticmethod
    def generate_email(domain=None):
        """Генерирует случайный email (если domain указан — подставляется свой)"""
        email = fake.email()
        if domain:
            username = email.split('@')[0]
            return f"{username}@{domain}"
        return email

    @staticmethod
    def generate_phone_number(country_code="+1"):
        """Генерирует случайный номер телефона"""
        return f"{country_code} {random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"