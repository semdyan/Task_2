import allure
import requests

from data import Urls

class UserData:
    @staticmethod
    @allure.step('Запрос на изменение данных пользователя')
    def patch_change_user_data(headers, payload):
        url = f'{Urls.BASE_URL}{Urls.USER_URL}'
        return requests.patch(url=url, headers=headers, json=payload)