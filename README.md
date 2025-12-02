# Task_2
API-tests

## В проекте организована структура файлов и директорий:
### methods - директория с файлами для хранения методов взаимодействия с эндпоинтами
- create_user_methods - методы для создания пользователя
- delete_user_methods - методы для удаления пользователя
- login_user_methods - методы для авторизации пользователя
- user_data_methods - методы для получения и изменения данных пользователя
- order_methods - методы для взаимодействия с заказом

### tests - директория с файлами тестов
- test_create_user.py - файл с тестами на создание пользователя
  TestCreateUser - класс с тестами на создание пользователя
  - test_create_user_success - проверка успешного сценария
  - test_create_user_are_tokens_in_response - проверка возврата токенов
  - test_create_user_existing_user_error - проверка ошибки существующего пользователя
  - test_create_user_missing_field_error - проверка ошибки отсутствия поля, параметризованный

- test_login_user.py - файл с тестами на авторизацию пользователя
  TestLoginUser - класс с тестами на авторизацию пользователя
  - test_login_user_successful - проверка успешной авторизации
  - test_login_user_are_tokens_in_response - проверка возврата токенов
  - test_login_user_missing_field_error - проверка ошибки отсутствия поля, параметризованный
  - test_login_incorrect_field_error - проверка ошибки некорректных данных, параметризованный

- test_change_user_data.py - файл с тестами на изменение данных пользователя
  TestChangeUserData - класс с тестами на изменение данных пользователя
  - test_change_user_data - проверка успешного изменения данных, параметризованный
  - test_change_user_data_invalid_token_error - проверка ошибки неавторизованного пользователя, параметризованный

- test_order.py - файл с тестами на взаимодействие с заказом
  TestCreateOrder - класс с тестами на создание заказа
  - test_create_order_full_ingredients_list_success - проверка успешного создания заказа с полным набором данных
  - test_create_order_no_token_success - проверка успешного создания заказа без авторизации
  - test_create_order_with_missing_ingredients_success - проверка успешного создания заказа без одного из ингредиентов, параметризованный
  - test_create_order_no_ingredients_error - проверка ошибки отсутствующих ингредиентов
  - test_create_order_incorrect_ingredient_hash_error - проверка ошибки некорректного хэша ингредиента
  
  TestGetOrders - класс с тестами на получение списка заказов
  - test_get_orders_with_token_success - проверка успешного получения заказов пользователя с авторизацией
  - test_get_orders_no_token_error - проверка ошибки проверка ошибки неавторизованного пользователя

## conftest.py - файл с фикстурами и общими методами
- generate_payload - генерирует body для запроса за создание пользователя
- create_and_return_user - создает пользователя и возвращает body, с которым он создан
- create_payload_for_login - формирует и возвращает body для запроса на авторизацию
- login_and_return_access_token - авторизует созданного пользователя и возвращает токен и body, с которым он создан
- generate_random_ingredients_list - создает случайный список ингредиентов всех типов для бургера 

## data.py - файл с данными для тестов
- Urls - класс с адресами

## requirements.txt - файл с необходимыми импортами