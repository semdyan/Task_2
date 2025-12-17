import allure
import requests

from data import Urls
from methods.login_user_methods import LoginUser

class DeleteUser:
    @staticmethod
    @allure.step('Delete user')
    def login_and_delete_user(payload):
        token = LoginUser.post_login_user(payload).json().get('accessToken')
        headers = {'Authorization': token}
        url = f'{Urls.BASE_URL}{Urls.USER_URL}'
        requests.delete(url=url, headers=headers)