import allure
import pytest

from methods.create_user_methods import CreateUser
from methods.delete_user_methods import DeleteUser

class TestCreateUser:
    @allure.title('Проверка что пользователь создается')
    def test_create_user_success(self, generate_payload):
        payload = generate_payload
        result = CreateUser.post_create_user(payload)
        assert result.status_code == 200 and result.json().get('success'), 'Вернулся некорректный ответ'
        DeleteUser.login_and_delete_user(payload)

    @allure.title('Проверка что возвращаются токены')
    def test_create_user_are_tokens_in_response(self, generate_payload):
        payload = generate_payload
        result = CreateUser.post_create_user(payload)
        assert result.json().get('accessToken') and result.json().get('refreshToken'), 'Не вернулись токены'
        DeleteUser.login_and_delete_user(payload)

    @allure.title('Проверка что нельзя зарегистрировать существующего пользователя')
    def test_create_user_existing_user_error(self, create_and_return_user):
        payload = create_and_return_user
        result = CreateUser.post_create_user(payload)
        assert (result.status_code == 403 and not result.json().get('success')
                and result.json().get('message') == 'User already exists'), 'Вернулся некорректный ответ'

    @allure.title('Проверка что нельзя зарегистрировать пользователя без обязательных полей')
    @pytest.mark.parametrize('missing_field', ['email', 'password', 'name'])
    def test_create_user_missing_field_error(self, generate_payload, missing_field):
        payload = generate_payload
        payload.pop(missing_field)
        result = CreateUser.post_create_user(payload)
        assert (result.status_code == 403 and not result.json().get('success')
                and result.json().get('message') == 'Email, password and name are required fields'), \
            'Вернулся некорректный ответ'