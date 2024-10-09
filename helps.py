from faker import Faker

class DataCreate:
    # функция генерации фэйковых валидных данных
    @staticmethod
    def generating_fake_valid_data_to_create_courier():
        fake = Faker("ru_RU")
        login = fake.user_name()
        password = fake.password()
        firstname = fake.first_name()
        data = {
            "login": login,
            "firstName": firstname,
            "password": password
        }

        return data

    # функция генерации фэйковых данных без поля "Login"
    @staticmethod
    def generating_fake_invalid_data_to_create_courier_without_login_field():
        fake = Faker("ru_RU")
        firstname = fake.first_name()
        password = fake.password()
        data = {
            "login": "",
            "firstName": firstname,
            "password": password
        }

        return data

    # функция генерации фэйковых данных без поля "Password"
    @staticmethod
    def generating_fake_invalid_data_to_create_courier_without_password_field():
        fake = Faker("ru_RU")
        login = fake.user_name()
        firstname = fake.first_name()
        data = {
            "login": login,
            "password": "",
            "firstName": firstname
        }

        return data

