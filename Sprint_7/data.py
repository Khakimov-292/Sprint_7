class AccountCourier:
    VALID_LOGIN = "oleg222"
    INCORRECT_LOGIN = "curaa"
    VALID_PASSWORD = "1234"
    INCORRECT_PASSWORD = "251485"
    NAME_COURIER = "oleg"

class Jsons:
    RECREATING_ONE_COURIER_JSON = {"code": 409,"message": "Этот логин уже используется. Попробуйте другой."}
    CREATE_COURIER_WITHOUT_LOGIN_JSON = {"code": 400,"message": "Недостаточно данных для создания учетной записи"}
    AUTHORIZATION_UNDER_INCORRECT_COURIER_JSON = {"code": 404,"message": "Учетная запись не найдена"}
    LOGIN_WITHOUT_PASSWORD_JSON = {"code": 400,"message":  "Недостаточно данных для входа"}



class OrderData:
    VALID_ORDER = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }

    ORDER_BLACK_AND_GREY = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK",
            "GREY"
        ]
    }

    ORDER_WITHOUT_COLOR = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        'color': []
    }
