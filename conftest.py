import random
import pytest

from data import Urls
from methods.create_user_methods import CreateUser
from methods.login_user_methods import LoginUser


@pytest.fixture(scope='function')
def generate_payload():
    email = f'{random.randint(1, 1000000)}@testdomain.com'
    password = f'{random.randint(1, 1000000)}'
    name = f'{random.randint(1, 1000000)}'
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload

@pytest.fixture(scope='function')
def create_and_return_user(generate_payload):
    payload = generate_payload
    url = f'{Urls.BASE_URL}{Urls.CREATE_USER_URL}'
    CreateUser.post_create_user(url, payload)
    return payload

@pytest.fixture(scope='function')
def login_and_return_access_token(create_and_return_user):
    payload = create_and_return_user
    url = f'{Urls.BASE_URL}{Urls.LOGIN_USER_URL}'
    token = LoginUser.post_login_user(url, payload).json()['accessToken']
    return token, payload
