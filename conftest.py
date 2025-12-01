import random
import pytest

from methods.create_user_methods import CreateUser
from methods.login_user_methods import LoginUser
from methods.order_methods import Order

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
    CreateUser.post_create_user(payload)
    return payload

@pytest.fixture(scope='function')
def login_and_return_access_token(create_and_return_user):
    payload = create_and_return_user
    token = LoginUser.post_login_user(payload).json()['accessToken']
    return token

@pytest.fixture(scope='function')
def generate_random_ingredients_list():
    all_ingredients = Order.get_ingredients().json().get('data')
    buns_ids = [ingredient['_id'] for ingredient in all_ingredients if ingredient.get('type') == 'bun']
    sauces_ids = [ingredient['_id'] for ingredient in all_ingredients if ingredient.get('type') == 'sauce']
    filling_ids = [ingredient['_id'] for ingredient in all_ingredients if ingredient.get('type') == 'main']
    bun = random.choice(buns_ids)
    sauce = random.choice(sauces_ids)
    filling = random.choice(filling_ids)
    ingredients_list = {
        'ingredients': [bun, sauce, filling]
    }
    return ingredients_list