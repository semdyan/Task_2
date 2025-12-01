import allure
import pytest
import random

from methods.login_user_methods import LoginUser

class TestLoginUser:
    @allure.title('Проверка что можно авторизоваться под существующим пользователем')
    def test_login_user_successful(self, create_payload_for_login):
        result = LoginUser.post_login_user(create_payload_for_login)
        assert result.status_code == 200 and result.json().get('success'), 'Вернулся некорректный ответ'

    @allure.title('Проверка что возвращаются токены')
    def test_login_user_are_tokens_in_response(self, create_payload_for_login):
        result = LoginUser.post_login_user(create_payload_for_login)
        assert result.json().get('accessToken') and result.json().get('refreshToken'), 'Не вернулись токены'

    @allure.title('Проверка что нельзя авторизоваться без обязательных полей')
    @pytest.mark.parametrize('missing_field', ['email', 'password'])
    def test_login_user_missing_field_error(self, create_payload_for_login, missing_field):
        payload = create_payload_for_login
        payload.pop(missing_field)
        result = LoginUser.post_login_user(payload)
        assert (result.status_code == 401 and not result.json().get('success')
                and result.json().get('message') == 'email or password are incorrect'), 'Вернулся некорректный ответ'

    @allure.title('Проверка что нельзя авторизоваться с некорректными данными')
    @pytest.mark.parametrize('incorrect_field', ['email', 'password'])
    def test_login_incorrect_field_error(self, create_payload_for_login, incorrect_field):
        payload = create_payload_for_login
        payload[incorrect_field] += str(random.randint(1, 1000000))
        result = LoginUser.post_login_user(payload)
        assert (result.status_code == 401 and not result.json().get('success')
                and result.json().get('message') == 'email or password are incorrect'), 'Вернулся некорректный ответ'