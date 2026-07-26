import requests
import allure
from data import Urls

@allure.epic("Stellar Burgers API")
@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.story("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_authorized_with_ingredients_success(self, created_user):
        _, token = created_user
        
        ingredients_resp = requests.get(Urls.INGREDIENTS)
        valid_ingredient = ingredients_resp.json()["data"][0]["_id"]
        
        ingredients_data = {"ingredients": [valid_ingredient]}
        headers = {"Authorization": token if "Bearer" in token else f"Bearer {token}"}
        
        response = requests.post(Urls.ORDERS, json=ingredients_data, headers=headers)
        
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.story("Создание заказа без авторизации")
    def test_create_order_unauthorized_success(self):
        ingredients_resp = requests.get(Urls.INGREDIENTS)
        valid_ingredient = ingredients_resp.json()["data"][0]["_id"]
        
        ingredients_data = {"ingredients": [valid_ingredient]}
        
        response = requests.post(Urls.ORDERS, json=ingredients_data)
        
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.story("Ошибка: создание заказа без ингредиентов")
    def test_create_order_no_ingredients_error(self, created_user):
        _, token = created_user
        ingredients_data = {"ingredients": []}
        headers = {"Authorization": token if "Bearer" in token else f"Bearer {token}"}
        
        response = requests.post(Urls.ORDERS, json=ingredients_data, headers=headers)
        
        assert response.status_code == 400
        assert response.json().get("success") is False

    @allure.story("Ошибка: создание заказа с неверным хешем ингредиента")
    def test_create_order_invalid_ingredients_error(self, created_user):
        _, token = created_user
        ingredients_data = {"ingredients": ["invalid hash 123"]}
        headers = {"Authorization": token if "Bearer" in token else f"Bearer {token}"}
        
        response = requests.post(Urls.ORDERS, json=ingredients_data, headers=headers)
        
        assert response.status_code == 500
