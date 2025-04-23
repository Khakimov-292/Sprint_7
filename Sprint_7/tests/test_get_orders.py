import requests

from urls import Urls


class TestGetOrders:
    def test_get_list_orders(self):
        response = requests.get(Urls.URL_orders)
        assert response.json()["orders"] != [] and response.status_code == 200