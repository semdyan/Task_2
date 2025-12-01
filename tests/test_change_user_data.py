import allure
import pytest
import random

from methods.user_data_methods import UserData
from data import Urls

class TestChangeUserData:
    @allure.title('Проверка, что можно поменять данные пользователя')
    @pytest.mark.parametrize('field_to_change', ['email', 'name'])
    def test_change_user_data(self, login_and_return_access_token, field_to_change):
        token, payload = login_and_return_access_token
        payload[field_to_change] += str(random.randint(0, 1000000))
        url = f'{Urls.BASE_URL}{Urls.USER_DATA_URL}'
        headers = {'Authorization': token}
        result = UserData.patch_change_user_data(url=url, headers=headers, payload=payload)
        assert (result.status_code == 200 and result.json().get('success')
                and result.json().get('user')[field_to_change] == payload[field_to_change]), 'Вернулся некорректный ответ'

    @allure.title('Проверка, что можно нельзя поменять данные пользователя без токена')
    @pytest.mark.parametrize('field_to_change', ['email', 'name'])
    def test_change_user_data_invalid_token_error(self, create_and_return_user, field_to_change):
        payload = create_and_return_user
        payload[field_to_change] += str(random.randint(0, 1000000))
        url = f'{Urls.BASE_URL}{Urls.USER_DATA_URL}'
        result = UserData.patch_change_user_data(url=url, headers=None, payload=payload)
        assert (result.status_code == 401 and result.json().get('success') == False
                and result.json().get('message') == 'You should be authorised'), 'Вернулся некорректный ответ'