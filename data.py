class Urls:
    # Базовый адрес учебного сервера из твоей доки
    BASE_URL = "https://education-services.ru"
    
    # Эндпоинты пользователя
    REGISTER = f"{BASE_URL}/auth/register"
    LOGIN = f"{BASE_URL}/auth/login"
    USER = f"{BASE_URL}/auth/user"
    
    # Эндпоинты заказов
    ORDERS = f"{BASE_URL}/orders"
    INGREDIENTS = f"{BASE_URL}/ingredients"
