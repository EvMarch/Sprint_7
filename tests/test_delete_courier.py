import allure
from couriers_requests import Courier
from data import DataTextAnswer


class TestDeleteCourier:

    @allure.title('Проверка удаления курьера')
    @allure.description('Отправляем запрос на удаление курьера и проверяем ответ')
    def test_delete_courier_success(self, courier_delete):
        courier_id = courier_delete
        response = Courier().courier_subsequent_deletion(courier_id["id"])
        assert response["status_code"] == 200
        assert response["response_text"] == '{"ok":true}'


    @allure.title('Проверка удаления курьера с')
    @allure.description('Отправляем запрос на удаление курьера с несущ.ID и проверяем ответ')
    def test_delete_courier_invalid_id_failed(self):
        courier_id = '123456'
        response = Courier().courier_subsequent_deletion(courier_id)
        assert response["status_code"] == 404
        assert DataTextAnswer.courier_id_not_found in response["response_text"]

    @allure.title('Проверка создания нового курьера')
    @allure.description('Отправляем запрос на удаление курьера без ID и проверяем ответ')
    def test_delete_courier_none_id_failed(self):
        courier_id = None
        response = Courier().courier_subsequent_deletion(courier_id)
        assert response["status_code"] == 500
        assert DataTextAnswer.invalid_syntax in response["response_text"]