import allure
import pytest
import requests
from couriers_requests import DataCourier, Courier
from endpoints import Endpoints
from urls import Urls
from data import DataTextAnswer

class TestLoginCourier:

    @allure.title('Проверка курьер может авторизоваться')
    @allure.description('Отправляем запрос на авторизацию в сервисе, проверяем ответ и удаляем курьера')
    def test_courier_login_success(self, courier):
        courier_data = courier
        response = Courier().courier_login_in_the_system_and_get_id_courier(courier_data["data"])
        assert response["status_code"] == 200
        assert response.get("id")

    @allure.title('Проверка для авторизации нужно передать все обязательные поля Login/Password')
    @allure.description('''Отправляем запрос на авторизацию в сервисе без заполнения обязательных полей Login/Password
                         и проверяем ответ''')
    @pytest.mark.parametrize('courier_data', [DataCourier.invalid_data_login_without_login,
                                           DataCourier.invalid_data_login_without_password])
    def test_courier_login_without_parameters_failed(self, courier_data):
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.login_courier}', data=courier_data)
        assert response.status_code == 400
        assert DataTextAnswer.need_more_data_login in response.text

    @allure.title('Проверка авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    @allure.description('Отправляем запрос на авторизацию в сервисе с несуществующими данными и проверяем ответ')
    def test_courier_login_without_null_login_failed(self):
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.login_courier}', data=DataCourier.null_data_login)
        assert response.status_code == 404
        assert DataTextAnswer.courier_login_not_found in response.text