import pytest

from couriers_requests import Courier


# фикстура регистрации курьера
@pytest.fixture()
def courier():
    courier_create = Courier().courier_registration_in_the_system_and_get_courier_data()
    yield courier_create


# фикстура авторизации и удаления курьера
@pytest.fixture()
def courier_delete():
    courier_create = Courier().courier_registration_in_the_system_and_get_courier_data()
    courier_login = Courier().courier_login_in_the_system_and_get_id_courier(courier_create["data"])
    yield courier_login
    Courier().courier_subsequent_deletion(courier_login["id"])
