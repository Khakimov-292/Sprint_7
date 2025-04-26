import allure
import requests

from data import Jsons
from helpers import register_new_courier_and_return_login_password, delete_courier
from urls import Urls


class TestCreateCourier:
    id_courier = None
    @allure.title('Проверка успешного создания курьера со всеми обязательными полями')
    def test_create_courier_success(self):
        data_courier = register_new_courier_and_return_login_password()
        response = requests.post(Urls.URL_create_and_delete_courier, data=data_courier)
        assert response.status_code == 201
        answer = response.json()
        self.id_courier = answer.get("id")
        delete_courier(self.id_courier)

    @allure.title('Проверка повторного создания одного и того же курьера')
    def test_recreating_one_courier(self):
        data_courier = register_new_courier_and_return_login_password()
        response1 = requests.post(Urls.URL_create_and_delete_courier, data=data_courier)
        response2 = requests.post(Urls.URL_create_and_delete_courier, data=data_courier)
        assert response1.status_code == 201
        assert response2.status_code == 409 and response2.json() == Jsons.RECREATING_ONE_COURIER_JSON
        delete_courier(self.id_courier)

    @allure.title('Проверка создания курьера без обязательного поля')
    def test_create_courier_without_login(self):
        payload = register_new_courier_and_return_login_password()
        data_courier = {"password": payload["password"], "firstName": payload["firstName"]}
        response = requests.post(Urls.URL_create_and_delete_courier, data=data_courier)
        assert response.json() == Jsons.CREATE_COURIER_WITHOUT_LOGIN_JSON and response.status_code == 400
        delete_courier(self.id_courier)
