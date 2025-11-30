import allure
import pytest
import random

from methods.login_user_methods import LoginUser
from data import Urls

class TestLoginUser:
    @allure.title('Проверка что можно авторизоваться под существующим пользователем')
    def test_login_user_successful(self, create_and_return_user):
        url = f'{Urls.BASE_URL}{Urls.LOGIN_USER_URL}'
        payload = create_and_return_user[0]
        payload.pop('name')
        result = LoginUser.post_login_user(url, payload)
        assert result.status_code == 200 and result.json().get('success')

    @allure.title('Проверка что возвращаются токены')
    def test_login_user_are_tokens_in_response(self, create_and_return_user):
        url = f'{Urls.BASE_URL}{Urls.LOGIN_USER_URL}'
        payload = create_and_return_user[0]
        payload.pop('name')
        result = LoginUser.post_login_user(url, payload)
        assert result.json().get('accessToken') and result.json().get('refreshToken')

    @allure.title('Проверка что нельзя авторизоваться без обязательных полей')
    @pytest.mark.parametrize('missing_field', ['email', 'password'])
    def test_login_user_missing_field_error(self, create_and_return_user, missing_field):
        url = f'{Urls.BASE_URL}{Urls.LOGIN_USER_URL}'
        payload = create_and_return_user[0]
        payload.pop('name')
        payload.pop(missing_field)
        result = LoginUser.post_login_user(url, payload)
        assert (result.status_code == 401 and not result.json().get('success')
                and result.json().get('message') == 'email or password are incorrect')

    @allure.title('Проверка что нельзя авторизоваться с некорректными данными')
    @pytest.mark.parametrize('incorrect_field', ['email', 'password'])
    def test_login_incorrect_field_error(self, create_and_return_user, incorrect_field):
        url = f'{Urls.BASE_URL}{Urls.LOGIN_USER_URL}'
        payload = create_and_return_user[0]
        payload.pop('name')
        payload[incorrect_field] += str(random.randint(1, 1000000))
        result = LoginUser.post_login_user(url, payload)
        assert (result.status_code == 401 and not result.json().get('success')
                and result.json().get('message') == 'email or password are incorrect')