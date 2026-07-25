import pytest
import requests
import random
import string
from urls import BASE_URL

@pytest.fixture
def user_data():
    # Генерируем случайные данные для каждого теста
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return {
        "email": f"alex_test_{random_str}@yandex.ru",
        "password": f"pass_{random_str}",
        "name": f"Alex_{random_str}"
    }

@pytest.fixture
def created_user(user_data):
    # Создаем юзера перед тестом и отдаем данные
    response = requests.post(f"{BASE_URL}/api/auth/register", json=user_data)
    token = response.json().get("accessToken")
    yield user_data, token
    # Удаляем юзера после теста (Teardown)
    if token:
        requests.delete(f"{BASE_URL}/api/auth/user", headers={"Authorization": token})
