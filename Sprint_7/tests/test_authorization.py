import requests
import allure

from data import AccountCourier, Jsons
from urls import Urls


class TestLoginCourier:
    @allure.title("Проверка авторизации курьера")
    def test_autorization_courier_success(self):
        data_courier = {"login": AccountCourier.VALID_LOGIN, "password": AccountCourier.VALID_PASSWORD}
        response = requests.post(Urls.URL_login_courier, data=data_courier)
        assert "id" in response.json() and response.status_code == 200

    @allure.title("Проверка авторизации под некорректным курьером")
    def test_autorization_under_incorrect_courier(self):
        data_courier = {"login": AccountCourier.INCORRECT_LOGIN, "password": AccountCourier.INCORRECT_PASSWORD}
        response = requests.post(Urls.URL_login_courier, data=data_courier)
        assert response.json() == Jsons.AUTHORIZATION_UNDER_INCORRECT_COURIER_JSON and response.status_code == 404

    @allure.title("Проверка авторизации без пароля")
    def test_login_without_password(self):
        data_courier = {"login": AccountCourier.VALID_LOGIN, "password": ""}
        response = requests.post(Urls.URL_login_courier, data=data_courier)
        assert response.json() == Jsons.LOGIN_WITHOUT_PASSWORD_JSON and response.status_code == 400
