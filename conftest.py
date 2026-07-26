import pytest
import requests
from data import Urls
from helpers import generate_user_data

@pytest.fixture
def created_user():
    """Фикстура создает уникального пользователя и удаляет его после теста"""
    payload = generate_user_data()
    response = requests.post(Urls.REGISTER, json=payload)
    
    token = response.json().get("accessToken")
    yield payload, response
    
    # Очистка данных после теста
    if token:
        headers = {"Authorization": token}
        requests.delete(Urls.USER, headers=headers)
