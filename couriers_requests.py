import requests

from endpoints import Endpoints
from urls import Urls

from helps import DataCreate

class DataCourier:
    # валидные данные для регистрации
    valid_data_login = DataCreate.generating_fake_valid_data_to_create_courier()

    # невалидные данные для регистрации без поля "Login"
    invalid_data_login_without_login = DataCreate.generating_fake_invalid_data_to_create_courier_without_login_field()

    # невалидные данные для регистрации без поля "Password"
    invalid_data_login_without_password = DataCreate.generating_fake_invalid_data_to_create_courier_without_password_field()

    # данные несуществующего курьера
    null_data_login = {
        "login": "test",
        "password": "test"
    }


class Courier:

    # функция регистрации в системе с возвратом ответа и данных курьера
    @staticmethod
    def courier_registration_in_the_system_and_get_courier_data():
        data = DataCreate.generating_fake_valid_data_to_create_courier()
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.create_courier}', data=data)
        return {"response_text": response.text, "status_code": response.status_code, "data": data}

    # функция логина в системе с возвратом ответа и id курьера
    @staticmethod
    def courier_login_in_the_system_and_get_id_courier(data):
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.login_courier}', data=data)
        return {"id": str(response.json()["id"]), "response_text": response.text, "status_code": response.status_code}

    # функция удаления курьера
    @staticmethod
    def courier_subsequent_deletion(id):
        response = requests.delete(f'{Urls.BASE_URL}{Endpoints.delete_courier}{id}')
        return {"response_text": response.text, "status_code": response.status_code}