import requests
import allure
from urls import BASE_URL

@allure.epic("Stellar Burgers API")
@allure.feature("Логин пользователя")
class TestLoginUser:

    @allure.story("Успешный вход под существующим пользователем")
    def test_login_existing_user_success(self, created_user):
        user_data, _ = created_user
        login_data = {"email": user_data["email"], "password": user_data["password"]}
        
        # Убран лишний /api из эндпоинта
        response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
        
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.story("Ошибка при входе с неверным логином и паролем")
    def test_login_wrong_credentials_error(self):
        wrong_data = {"email": "invalid_user_999@yandex.ru", "password": "wrong_password"}
        
        # Убран лишний /api из эндпоинта
        response = requests.post(f"{BASE_URL}/auth/login", json=wrong_data)
        
        assert response.status_code == 401
        assert response.json().get("success") is False
