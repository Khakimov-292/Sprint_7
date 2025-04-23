import requests
import allure

from data import Jsons, AccountCourier
from urls import Urls


class TestCreateCourier:
    @allure.title('Проверка успешного создания курьера со всеми обязательными полями')
    def test_create_courier_success(self):
        data_courier = {"login": AccountCourier.VALID_LOGIN, "password": AccountCourier.VALID_PASSWORD, "firstName": AccountCourier.NAME_COURIER}
        response = requests.post(Urls.URL_create_courier, data=data_courier)
        assert response.status_code == 201

    @allure.title('Проверка повторного создания одного и того же курьера')
    def test_recreating_one_courier(self):
        data_courier = {"login": AccountCourier.VALID_LOGIN, "password": AccountCourier.VALID_PASSWORD, "firstName": AccountCourier.NAME_COURIER}
        response = requests.post(Urls.URL_create_courier, data=data_courier)
        assert response.status_code == 409 and response.json() == Jsons.RECREATING_ONE_COURIER_JSON

    @allure.title('Проверка создания курьера без обязательного поля')
    def test_create_courier_without_login(self):
        data_courier = {"password": AccountCourier.VALID_PASSWORD, "firstName": AccountCourier.NAME_COURIER}
        response = requests.post(Urls.URL_create_courier, data=data_courier)
        assert response.json() == Jsons.CREATE_COURIER_WITHOUT_LOGIN_JSON and response.status_code == 400

