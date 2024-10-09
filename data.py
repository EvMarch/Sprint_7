class DataOrder:
    # данные для заказа самоката без цвета
    data = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Ленина, 15",
        "metroStation": 1,
        "phone": "+7 800 5553535",
        "rentTime": 4,
        "deliveryDate": "2024-03-30",
        "comment": "Только наличными, сдача с 5000",
    }

class DataTextAnswer:
    login_not_avaiable = "Этот логин уже используется"
    need_more_data_sign = "Недостаточно данных для создания учетной записи"
    courier_id_not_found = "Курьера с таким id нет"
    invalid_syntax = "invalid input syntax"
    need_more_data_login =  "Недостаточно данных для входа"
    courier_login_not_found = "Учетная запись не найдена"
    color_order = "track"
    order_list = "track"