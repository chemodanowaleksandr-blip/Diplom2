import pytest
import requests
from data import Urls
from helpers import generate_user_data

@pytest.fixture
def created_user():
    """Фикстура создает уникального пользователя и удаляет его после теста"""
    payload = generate_user_data()
    
    # Берем эндпоинт REGISTER из класса Urls
    response = requests.post(Urls.REGISTER, json=payload)
    
    token = response.json().get("accessToken")
    yield payload, token
    
    # Очистка данных после теста через эндпоинт USER
    if token:
        headers = {"Authorization": token}
        requests.delete(Urls.USER, headers=headers)
