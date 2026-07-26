class Urls:
    # Базовый URL для этого проекта (может быть nomoreparties или education-services, используйте ваш текущий)
    BASE_URL = "https://education-services.ru"
    
    REGISTER = f"{BASE_URL}/api/auth/register"
    LOGIN = f"{BASE_URL}/api/auth/login"
    USER = f"{BASE_URL}/api/auth/user"
    ORDERS = f"{BASE_URL}/api/orders"
    INGREDIENTS = f"{BASE_URL}/api/ingredients"
