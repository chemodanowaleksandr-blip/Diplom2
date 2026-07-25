import requests
import allure
from urls import BASE_URL

@allure.epic("Stellar Burgers API")
@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.story("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_authorized_with_ingredients_success(self, created_user):
        _, token = created_user
        ingredients_data = {"ingredients": ["61c0c5cd223ce5001b617f61"]}
        headers = {"Authorization": token}
        response = requests.post(f"{BASE_URL}/api/orders", json=ingredients_data, headers=headers)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.story("Создание заказа без авторизации")
    def test_create_order_unauthorized_success(self):
        ingredients_data = {"ingredients": ["61c0c5cd223ce5001b617f61"]}
        response = requests.post(f"{BASE_URL}/api/orders", json=ingredients_data)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.story("Ошибка: создание заказа без ингредиентов")
    def test_create_order_no_ingredients_error(self, created_user):
        _, token = created_user
        ingredients_data = {"ingredients": []}
        headers = {"Authorization": token}
        response = requests.post(f"{BASE_URL}/api/orders", json=ingredients_data, headers=headers)
        assert response.status_code == 400
        assert response.json().get("success") is False

    @allure.story("Ошибка: создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_ingredients_error(self, created_user):
        _, token = created_user
        ingredients_data = {"ingredients": ["invalid_hash_123"]}
        headers = {"Authorization": token}
        response = requests.post(f"{BASE_URL}/api/orders", json=ingredients_data, headers=headers)
        assert response.status_code == 500
