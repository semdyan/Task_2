import allure
import pytest
import random

from methods.login_user_methods import LoginUser
from data import ResponseMessages

class TestLoginUser:
    @allure.title('Проверка что можно авторизоваться под существующим пользователем')
    def test_login_user_successful(self, create_payload_for_login):
        result = LoginUser.post_login_user(create_payload_for_login)
        assert result.status_code == 200, 'Вернулся некорректный код ответа'
        assert result.json().get('success'), 'Вернулось некорректное значение success'
        assert result.json().get('accessToken'), 'Не вернулся accessToken'
        assert result.json().get('refreshToken'), 'Не вернулся refreshToken'

    @allure.title('Проверка что нельзя авторизоваться без обязательных полей')
    @pytest.mark.parametrize('missing_field', ['email', 'password'])
    def test_login_user_missing_field_error(self, create_payload_for_login, missing_field):
        payload = create_payload_for_login
        payload.pop(missing_field)
        result = LoginUser.post_login_user(payload)
        assert result.status_code == 401, 'Вернулся некорректный код ответа'
        assert not result.json().get('success'), 'Вернулось некорректное значение success'
        assert result.json().get('message') == ResponseMessages.INCORRECT_CREDENTIALS_MESSAGE, 'Вернулся некорректный текст ответа'

    @allure.title('Проверка что нельзя авторизоваться с некорректными данными')
    @pytest.mark.parametrize('incorrect_field', ['email', 'password'])
    def test_login_incorrect_field_error(self, create_payload_for_login, incorrect_field):
        payload = create_payload_for_login
        payload[incorrect_field] += str(random.randint(1, 1000000))
        result = LoginUser.post_login_user(payload)
        assert result.status_code == 401, 'Вернулся некорректный код ответа'
        assert not result.json().get('success'), 'Вернулось некорректное значение success'
        assert result.json().get('message') == ResponseMessages.INCORRECT_CREDENTIALS_MESSAGE, 'Вернулся некорректный текст ответа'