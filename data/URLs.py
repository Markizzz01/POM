# data/URLs.py — ссылки на страницы
import os
from dotenv import load_dotenv
load_dotenv()
STAGE = os.getenv("STAGE")

class Urls:
    BASE = "https://www.saucedemo.com"                                     # Базовый URL
    LOGIN = f"{BASE}/"                                                      # Страница логина
    PRODUCT = f"{BASE}/inventory.html"                                       # Страница товаров
    CART = f"{BASE}/cart.html"                                               # Корзина
    CHECKOUNT = f"{BASE}/checkout-step-one.html"                             # Оформление заказа
    FINISH = f"{BASE}/checkout-complete.html"                                 # Завершение покупки

