import pytest
import requests
import allure

from data import OrderData
from urls import Urls


class TestCreateOrder:
    @allure.title("Проверка создания заказа")
    @pytest.mark.parametrize('order_data', [
        OrderData.VALID_ORDER, OrderData.ORDER_BLACK_AND_GREY,
        OrderData.ORDER_WITHOUT_COLOR
    ])
    def test_create_order_to_color_black(self,order_data):
        order = order_data
        response = requests.post(Urls.URL_orders, json=order, timeout=5)
        assert "track" in response.json() and response.status_code == 201
