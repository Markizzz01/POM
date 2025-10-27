import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture(scope="class")
def driver(request):
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(20)

    # Привязываем driver к тестовому классу
    request.cls.driver = driver

    yield
    driver.quit()


@pytest.fixture(autouse=True)
def setup_environment_properties():
    # Создаем папку allure-results, если её нет
    os.makedirs("allure-results", exist_ok=True)
    properties = {
        "STAGE": "AQA",
        "BROWSER": "Chrome"
    }
    with open("allure-results/environment.properties", "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")