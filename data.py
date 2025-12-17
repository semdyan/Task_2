class Urls:
    BASE_URL = 'https://stellarburgers.education-services.ru'
    CREATE_USER_URL = '/api/auth/register'
    LOGIN_USER_URL = '/api/auth/login'
    USER_URL = '/api/auth/user'
    ORDERS_URL = '/api/orders'
    INGREDIENTS_DATA_URL = '/api/ingredients'

class ResponseMessages:
    UNAUTHORIZED_USER_MESSAGE = 'You should be authorised'
    EXISTING_USER_MESSAGE = 'User already exists'
    MISSING_FIELD_MESSAGE = 'Email, password and name are required fields'
    INCORRECT_CREDENTIALS_MESSAGE = 'email or password are incorrect'
