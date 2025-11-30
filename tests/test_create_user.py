import allure
import pytest

from methods.create_user_methods import CreateUser
from data import Urls

@allure.title('Проверка что пользователь создается')
def test_create_user_success(generate_payload):
    url = f'{Urls.BASE_URL}{Urls.CREATE_USER_URL}'
    payload = generate_payload
    result = CreateUser.post_create_user(url, payload)
    assert result.status_code == 200 and result.json().get('success') == True

@allure.title('Проверка что возвращаются токены')
def test_create_user_are_tokens_in_response(generate_payload):
    url = f'{Urls.BASE_URL}{Urls.CREATE_USER_URL}'
    payload = generate_payload
    result = CreateUser.post_create_user(url, payload)
    assert result.json().get('accessToken') and result.json().get('refreshToken')

@allure.title('Проверка что нельзя зарегистрировать существующего пользователя')
def test_create_user_existing_user_error(create_and_return_user):
    url = f'{Urls.BASE_URL}{Urls.CREATE_USER_URL}'
    payload = create_and_return_user[0]
    result = CreateUser.post_create_user(url, payload)
    assert (result.status_code == 403 and result.json().get('success') == False
            and result.json().get('message') == 'User already exists')

@allure.title('Проверка что нельзя зарегистрировать пользователя без обязательных полей')
@pytest.mark.parametrize('missing_field', ['email', 'password', 'name'])
def test_create_user_missing_field_error(generate_payload, missing_field):
    payload = generate_payload
    payload.pop(missing_field)
    url = f'{Urls.BASE_URL}{Urls.CREATE_USER_URL}'
    result = CreateUser.post_create_user(url, payload)
    assert (result.status_code == 403 and result.json().get('success') == False
            and result.json().get('message') == 'Email, password and name are required fields')