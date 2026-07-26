import pytest
import requests
from urls import BASE_URL
from helpers import generate_user_data

@pytest.fixture
def created_user():
    """Фикстура создает уникального пользователя и удаляет его после теста"""
    payload = generate_user_data()
    
    # Склеиваем BASE_URL с эндпоинтом регистрации
    response = requests.post(f"{BASE_URL}/auth/register", json=payload)
    
    token = response.json().get("accessToken")
    yield payload, token
    
    # Очистка данных после теста
    if token:
        headers = {"Authorization": token}
        requests.delete(f"{BASE_URL}/auth/user", headers=headers)
