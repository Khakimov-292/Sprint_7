import random
import string
import requests

from urls import Urls


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def register_new_courier_and_return_login_password():
    payload = {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }
    return payload

def delete_courier(id_courier):
    if id_courier is not None:
        delete_response = requests.delete(f"{Urls.URL_create_and_delete_courier}/{id_courier}")
        delete_data = delete_response.json()
        assert delete_response.status_code == 200, f"Ошибка удаления: {delete_data}"
        assert delete_data == {'ok': True}, f"Ошибка удаления: {delete_data}"
    else:
        pass
