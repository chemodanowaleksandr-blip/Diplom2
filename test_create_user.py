import requests
import allure
from data import Urls
from helpers import generate_user_data

class TestCreateUser:

    @allure.story("Ошибка: создание пользователя при заполнении не всех обязательных полей")
    def test_create_user_missing_field_error(self, created_user):
        # Распаковываем кортеж из фикстуры (данные и токен)
        user_payload, token = created_user
        
        # Создаем копию данных и удаляем одно из обязательных полей (например, email)
        wrong_payload = user_payload.copy()
        if "email" in wrong_payload:
            del wrong_payload["email"]
            
        # Отправляем запрос с неполными данными
        response = requests.post(Urls.REGISTER, json=wrong_payload)
        
        # Проверяем, что сервер вернул ошибку 403 Forbidden
        assert response.status_code == 403
        assert response.json().get("message") == "Email, password and name are required fields"

    @allure.story("Успешное создание уникального пользователя")
    def test_create_unique_user_success(self):
        payload = generate_user_data()
        response = requests.post(Urls.REGISTER, json=payload)
        
        assert response.status_code == 200
        assert response.json().get("success") is True
        
        # Чистим за собой созданного пользователя, если сервер вернул токен
        token = response.json().get("accessToken")
        if token:
            headers = {"Authorization": token}
            requests.delete(Urls.USER, headers=headers)

    @allure.story("Ошибка: создание пользователя, который уже зарегистрирован")
    def test_create_duplicate_user_error(self, created_user):
        user_payload, _ = created_user
        
        # Пытаемся повторно зарегистрировать того же пользователя
        response = requests.post(Urls.REGISTER, json=user_payload)
        
        assert response.status_code == 403
        assert response.json().get("message") == "User already exists"
