import random
import string

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_user_data():
    unique_part = generate_random_string(6)
    return {
        "email": f"test_user_{unique_part}@yandex.ru",
        "password": f"pass_{unique_part}",
        "name": f"User_{unique_part}"
    }
