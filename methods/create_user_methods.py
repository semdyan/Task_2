import allure
import requests


class CreateUser:

    @staticmethod
    @allure.step('Запрос на создание пользователя')
    def post_create_user(url, payload):
        result = requests.post(url=url, json=payload)
        return result



