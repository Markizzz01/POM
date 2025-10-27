# meta_locator.py — мета-класс, который автоматически превращает строковые локаторы в кортежи
# Например, если указать просто "//button", он превратится в ("xpath", "//button")

class MetaLocator(type):

    def __new__(cls, name, bases, attrs):
        # Перебираем все атрибуты (переменные) класса
        for key, value in attrs.items():
            if isinstance(value, str):  # Если атрибут — строка
                if value.startswith("//") or value.startswith(".//") or value.startswith("(//"):
                    attrs[key] = ("xpath", value)  # Автоматически превращаем в XPath локатор
                elif value.startswith(".") or value.startswith("#"):
                    attrs[key] = ("css selector", value)  # Или CSS-селектор
        return type.__new__(cls, name, bases, attrs)