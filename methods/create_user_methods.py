import allure
import requests

class CreateUser:
    @staticmethod
    @allure.step('Запрос на создание пользователя')
    def post_create_user(url, payload):
        return requests.post(url=url, json=payload)



