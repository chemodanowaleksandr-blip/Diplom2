import requests
import allure
from urls import BASE_URL

@allure.epic("Stellar Burgers API")
@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.story("Успешное создание уникального пользователя")
    def test_create_unique_user_success(self, user_data):
        response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
        
        assert response.status_code == 200
        assert response.json().get("success") is True
        
        token = response.json().get("accessToken")
        if token:
            requests.delete(f"{BASE_URL}/auth/user", headers={"Authorization": token})

    @allure.story("Ошибка: создание пользователя, который уже зарегистрирован")
    def test_create_duplicate_user_error(self, created_user):
        user_data, _ = created_user
        response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
        
        assert response.status_code == 403
        assert response.json().get("message") == "User already exists"

    @allure.story("Ошибка: создание пользователя при заполнении не всех обязательных полей")
    def test_create_user_missing_field_error(self, user_data):
        user_data["email"] = ""
        response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
        
        assert response.status_code == 403
        assert response.json().get("message") == "Email, password and name are required fields"
