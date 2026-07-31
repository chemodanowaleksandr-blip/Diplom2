import pytest
import requests
import allure
from data import urls
from helpers import generate_user_data

@allure.epic("Stellar Burgers API")
@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.story("Ошибка: создание пользователя при заполнении не всех обязательных полей")
    def test_create_user_missing_field_error(self, created_user):
        # Разворачиваем данные из фикстуры, чтобы получить готовый payload
        user_payload, _ = created_user
        
        # Создаем копию данных и удаляем одно из обязательных полей (например, email)
        wrong_payload = user_payload.copy()
        if "email" in wrong_payload:
            del wrong_payload["email"]

        # Отправляем запрос с неполными данными
        response = requests.post(urls.REGISTER, json=wrong_payload)

        # Проверяем, что сервер вернул ошибку 403 Forbidden
        assert response.status_code == 403
        assert response.json().get("message") == "Email, password and name are required fields"

    @allure.story("Успешное создание уникального пользователя")
    def test_create_user_success(self, created_user):
        # Фикстура сама создала пользователя и вернула нам его payload и токен
        _, token = created_user

        # Проверяем, что токен успешно сгенерирован (значит, юзер создан на сервере)
        assert token is not None
