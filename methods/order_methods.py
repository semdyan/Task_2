import allure
import requests

from data import Urls

class Order:
    @staticmethod
    @allure.step('Запрос на создание заказа')
    def post_create_order(payload, token=None):
        if token:
            headers = {'Authorization': token}
        else: headers = None
        url = f'{Urls.BASE_URL}{Urls.ORDERS_URL}'
        return requests.post(url, headers=headers, json=payload)

    @staticmethod
    @allure.step('Запрос на получение данных об ингредиентах')
    def get_ingredients():
        url = f'{Urls.BASE_URL}{Urls.INGREDIENTS_DATA_URL}'
        return requests.get(url)

    @staticmethod
    @allure.step('Запрос на получение данных о заказах пользователя')
    def get_user_orders(token=None):
        headers = {'Authorization': token}
        url = f'{Urls.BASE_URL}{Urls.ORDERS_URL}'
        return requests.get(url, headers=headers)