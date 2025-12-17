import allure
import requests

from data import Urls

class LoginUser:
    @staticmethod
    @allure.step('Запрос на авторизацию пользователя')
    def post_login_user(payload):
        url = f'{Urls.BASE_URL}{Urls.LOGIN_USER_URL}'
        return requests.post(url=url, json=payload)
