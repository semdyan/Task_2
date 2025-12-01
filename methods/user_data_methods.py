import allure
import requests

class UserData:
    @staticmethod
    @allure.step('Запрос на изменение данных пользователя')
    def patch_change_user_data(url, headers, payload):
        return requests.patch(url=url, headers=headers, json=payload)