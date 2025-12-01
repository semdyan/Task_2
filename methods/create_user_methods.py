import allure
import requests

from data import Urls

class CreateUser:
    @staticmethod
    @allure.step('Запрос на создание пользователя')
    def post_create_user(payload):
        url = f'{Urls.BASE_URL}{Urls.CREATE_USER_URL}'
        return requests.post(url=url, json=payload)



