import allure
import pytest

from methods.create_user_methods import CreateUser
from data import ResponseMessages

class TestCreateUser:
    @allure.title('Проверка что пользователь создается')
    def test_create_user_success(self, create_user_and_return_response):
        response = create_user_and_return_response
        assert response.status_code == 200, 'Вернулся некорректный код ответа'
        assert response.json().get('success'), 'Вернулось некорректное значение success'
        assert response.json().get('accessToken'), 'Не вернулся accessToken'
        assert response.json().get('refreshToken'), 'Не вернулся refreshToken'


    @allure.title('Проверка что нельзя зарегистрировать существующего пользователя')
    def test_create_user_existing_user_error(self, create_user_and_return_payload):
        payload = create_user_and_return_payload
        result = CreateUser.post_create_user(payload)
        assert result.status_code == 403, 'Вернулся некорректный код ответа'
        assert not result.json().get('success'), 'Вернулось некорректное значение success'
        assert result.json().get('message') == ResponseMessages.EXISTING_USER_MESSAGE, 'Вернулся некорректный текст ответа'

    @allure.title('Проверка что нельзя зарегистрировать пользователя без обязательных полей')
    @pytest.mark.parametrize('missing_field', ['email', 'password', 'name'])
    def test_create_user_missing_field_error(self, generate_payload, missing_field):
        payload = generate_payload
        payload.pop(missing_field)
        result = CreateUser.post_create_user(payload)
        assert result.status_code == 403, 'Вернулся некорректный код ответа'
        assert not result.json().get('success'), 'Вернулось некорректное значение success'
        assert result.json().get('message') == ResponseMessages.MISSING_FIELD_MESSAGE, 'Вернулся некорректный текст ответа'