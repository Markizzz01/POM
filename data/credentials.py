# data/credentials.py — креды пользователя
import os
from dotenv import load_dotenv
load_dotenv()

class Credentials:
    LOGIN = os.getenv("AQA_LOGIN")                                         # Логин из .env
    PASSWORD = os.getenv("AQA_PASSWORD")                                    # Пароль из .env
