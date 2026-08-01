import pytest
import requests
import allure
import data
from helpers import generate_user_data

# Автоматически берём ссылки, даже если в data.py написано Urls с большой буквы
urls = getattr(data, "urls", getattr(data, "Urls", data))

@allure.epic("Stellar Burgers API")
@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.story("Ошибка: создание пользователя при заполнении не всех обязательных полей")
    def test_create_user_missing_field_error(self):
        user_payload = generate_user_data()

        wrong_payload = user_payload.copy()
        # Избавляемся от if: безопасное удаление поля в одну строчку через pop
        wrong_payload.pop("email", None)

        with allure.step("Отправка POST-запроса на регистрацию с неполными данными"):
            response = requests.post(urls.REGISTER, json=wrong_payload)

        assert response.status_code == 403
        assert response.json().get("message") == "Email, password and name are required fields"

    @allure.story("Успешное создание уникального пользователя")
    def test_create_user_success(self):
        # Генерируем чистые данные для нового юзера
        payload = generate_user_data()
        
        # Запрос выполняется явно в тесте, как просила Ирина
        with allure.step("Отправка POST-запроса на регистрацию уникального пользователя"):
            response = requests.post(urls.REGISTER, json=payload)

        # Проверяем успешность создания
        assert response.status_code == 200
        assert response.json().get("success") is True
        
        # Получаем токен созданного юзера, чтобы вручную почистить базу в конце теста
        token = response.json().get("accessToken")
        
        # Очистка данных (Teardown) прямо в конце теста, без костылей и фикстур
        if token:
            with allure.step("Удаление созданного пользователя для очистки базы данных"):
                headers = {"Authorization": token}
                requests.delete(urls.USER, headers=headers)
