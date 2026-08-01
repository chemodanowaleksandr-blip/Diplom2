import pytest
import requests
from data import Urls
from helpers import generate_user_data

@pytest.fixture
def created_user():
    payload = generate_user_data()
    
    # Заголовки, чтобы сервер думал, что запрос отправлен из Chrome
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    response = requests.post(Urls.REGISTER, json=payload, headers=headers)
    
    if response.status_code == 429:
        token = None
    else:
        token = response.json().get("accessToken") if response.status_code == 200 else None
        
    yield payload, token
    
    if token:
        delete_headers = {
            "Authorization": token,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        requests.delete(Urls.USER, headers=delete_headers)
