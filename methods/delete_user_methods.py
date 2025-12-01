import allure
import requests

from data import Urls

class DeleteUser:
    @staticmethod
    @allure.step('Delete user')
    def delete_user(token):
        headers = {'Authorization': token}
        url = f'{Urls.BASE_URL}{Urls.USER_URL}'
        requests.delete(url=url, headers=headers)