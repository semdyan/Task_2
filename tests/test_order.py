import allure
import pytest

from methods.order_methods import Order

class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа с полным списком ингредиентов')
    def test_create_order_full_ingredients_list_success(self, login_and_return_access_token,
                                                        generate_random_ingredients_list):
        token = login_and_return_access_token
        ingredient_list = generate_random_ingredients_list
        response = Order().post_create_order(token=token, payload=ingredient_list)
        assert response.status_code == 200 and response.json().get('success'), 'Вернулся некорректный ответ'

    @allure.title('Проверка успешного создания заказа без авторизации')
    def test_create_order_no_token_success(self, generate_random_ingredients_list):
        ingredient_list = generate_random_ingredients_list
        response = Order().post_create_order(payload=ingredient_list)
        assert response.status_code == 200 and response.json().get('success'), 'Вернулся некорректный ответ'

    @allure.title('Проверка успешного создания заказа без отдельных ингредиентов')
    @pytest.mark.parametrize('missing_ingredient', [0, 1, 2])
    def test_create_order_with_missing_ingredients_success(self, generate_random_ingredients_list,
                                                             missing_ingredient):
        ingredient_list = generate_random_ingredients_list
        ingredient_list.get('ingredients').pop(missing_ingredient)
        response = Order().post_create_order(payload=ingredient_list)
        assert response.status_code == 200 and response.json().get('success'), 'Вернулся некорректный ответ'

    @allure.title('Проверка что нельзя создать заказ без ингредиентов')
    def test_create_order_no_ingredients_error(self):
        ingredient_list = {}
        response = Order().post_create_order(payload=ingredient_list)
        assert response.status_code == 400 and not response.json().get('success'), 'Вернулся некорректный ответ'

    @allure.title('Проверка что нельзя создать заказ с некорректным хешем ингредиента')
    def test_create_order_incorrect_ingredient_hash_error(self, generate_random_ingredients_list):
        ingredient_list = generate_random_ingredients_list
        ingredient_list.get('ingredients')[0] += '1'
        response = Order().post_create_order(payload=ingredient_list)
        assert response.status_code == 500, 'Вернулся некорректный ответ'

class TestGetOrders:
    @allure.title('Проверка успешного получения заказов пользователя c авторизацией')
    def test_get_orders_with_token_success(self, login_and_return_access_token, generate_random_ingredients_list):
        ingredients_list = generate_random_ingredients_list
        token = login_and_return_access_token
        Order().post_create_order(token=token, payload=ingredients_list)
        response = Order().get_user_orders(token=token)
        expected_ingredients_list = ingredients_list.get('ingredients')
        actual_ingredients_list = response.json().get('orders')[0].get('ingredients')
        assert (response.status_code == 200 and response.json().get('success')
                and actual_ingredients_list == expected_ingredients_list), 'Вернулся некорректный ответ'

    @allure.title('Проверка ошибки при попытке получить заказы пользователя без авторизации')
    def test_get_orders_no_token_error(self, login_and_return_access_token, generate_random_ingredients_list):
        ingredients_list = generate_random_ingredients_list
        token = login_and_return_access_token
        Order().post_create_order(token=token, payload=ingredients_list)
        response = Order().get_user_orders()
        assert (response.status_code == 401 and not response.json().get('success')
                and response.json().get('message') == 'You should be authorised'), 'Вернулся некорректный ответ'