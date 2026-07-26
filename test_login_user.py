import requests
import allure
from data import Urls  # Импортируем класс Urls вместо BASE_URL

@allure.epic("Stellar Burgers API")
@allure.feature("Логин пользователя")
class TestLoginUser:

    @allure.story("Успешный вход под существующим пользователем")
    def test_login_existing_user_success(self, created_user):
        user_data, _ = created_user
        login_data = {"email": user_data["email"], "password": user_data["password"]}
        
        # Меняем BASE_URL на Urls.LOGIN
        response = requests.post(Urls.LOGIN, json=login_data)
        
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.story("Ошибка при входе с неверным логином и паролем")
    def test_login_wrong_credentials_error(self):
        wrong_data = {"email": "invalid_user_999@yandex.ru", "password": "wrong_password"}
        
        # Меняем BASE_URL на Urls.LOGIN
        response = requests.post(Urls.LOGIN, json=wrong_data)
        
        assert response.status_code == 401
        assert response.json().get("success") is False
