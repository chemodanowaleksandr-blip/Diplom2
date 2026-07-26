import pytest
import requests
from data import Urls
from helpers import generate_user_data

@pytest.fixture
def created_user():
    payload = generate_user_data()
    response = requests.post(Urls.REGISTER, json=payload)
    
    # Если сервер забанил IP гитхаба, не пытаемся парсить пустой JSON
    if response.status_code == 429:
        token = None
    else:
        token = response.json().get("accessToken") if response.status_code == 200 else None
        
    yield payload, token
    
    if token:
        headers = {"Authorization": token}
        requests.delete(Urls.USER, headers=headers)
