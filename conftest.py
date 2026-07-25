import pytest
import requests
import random
import string
from urls import BASE_URL

@pytest.fixture
def user_data():
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return {
        "email": f"alex_test_{random_str}@yandex.ru",
        "password": f"pass_{random_str}",
        "name": f"Alex_{random_str}"
    }

@pytest.fixture
def created_user(user_data):
    response = requests.post(f"{BASE_URL}/api/auth/register", json=user_data)
    token = response.json().get("accessToken")
    yield user_data, token
    if token:
        requests.delete(f"{BASE_URL}/api/auth/user", headers={"Authorization": token})
