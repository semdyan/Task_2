import allure
import requests

class LoginUser:
    @staticmethod
    @allure.step('Запрос на авторизацию пользователя')
    def post_login_user(url, payload):
        return requests.post(url=url, json=payload)