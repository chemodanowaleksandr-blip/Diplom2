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
    def test_create_user_missing_field_error(self, created_user):
        user_payload, _ = created_user

        wrong_payload = user_payload.copy()
        if "email" in wrong_payload:
            del wrong_payload["email"]

        with allure.step("Отправка POST-запроса на регистрацию с неполными данными"):
            response = requests.post(urls.REGISTER, json=wrong_payload)

        assert response.status_code == 403
        assert response.json().get("message") == "Email, password and name are required fields"

    @allure.story("Успешное создание уникального пользователя")
    def test_create_user_success(self, created_user):
        _, token = created_user
        assert token is not None
