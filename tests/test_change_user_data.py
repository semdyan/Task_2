import allure
import pytest
import random

from methods.user_data_methods import UserData
from data import ResponseMessages

class TestChangeUserData:
    @allure.title('Проверка, что можно поменять данные пользователя')
    @pytest.mark.parametrize('field_to_change', ['email', 'name'])
    def test_change_user_data(self, login_and_return_access_token, field_to_change):
        token, payload = login_and_return_access_token
        payload[field_to_change] += str(random.randint(0, 1000000))
        headers = {'Authorization': token}
        result = UserData.patch_change_user_data(headers=headers, payload=payload)
        assert result.status_code == 200 and result.json().get('success'), 'Вернулся некорректный код ответа'
        assert result.json().get('user')[field_to_change] == payload[field_to_change], 'Вернулся некорректный текст ответа'

    @allure.title('Проверка, что нельзя поменять данные пользователя без токена')
    @pytest.mark.parametrize('field_to_change', ['email', 'name'])
    def test_change_user_data_invalid_token_error(self, create_and_return_user, field_to_change):
        payload = create_and_return_user
        payload[field_to_change] += str(random.randint(0, 1000000))
        result = UserData.patch_change_user_data(headers=None, payload=payload)
        assert result.status_code == 401, 'Вернулся некорректный код ответа'
        assert result.json().get('success') == False, 'Вернулось некорректное значение success'
        assert result.json().get('message') == ResponseMessages.UNAUTHORIZED_USER_MESSAGE, 'Вернулся некорректный текст ответа'