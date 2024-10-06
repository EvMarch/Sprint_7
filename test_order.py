import json
import allure
import pytest
import requests
from helps import DataOrder
from endpoints import Endpoints
from urls import Urls


class TestOrderCreate:

    @allure.title('Проверка оформления заказа с разным набором цветов')
    @allure.description('Отправляем запрос с указаникм одного из цветов; оба цвета; можно не указывать цвет')
    @pytest.mark.parametrize('color', [{"color": ["BLACK"]}, {"color": ["GREY"]}, {"color": ["BLACK", "GRAY"]}, {"color": [""]}])
    def test_create_order_success(self, color):
        headers = {"Content-type": "application/json"}
        data = DataOrder.data
        data.update(color)
        data = json.dumps(data)
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.create_order}', headers=headers, data=data)
        assert response.status_code == 201
        assert "track" in response.text