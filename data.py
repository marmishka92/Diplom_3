import allure
from faker import Faker

class Person:
    name = 'Екатерина'
    data = {"email": f'katya2025python@yandex.ru',
            "password": f'12345678'}

    email = 'katya2025python@yandex.ru'
    password =  '123456789'


class RegUser:

    @staticmethod
    @allure.step('Генератор')
    def create_user_new():
        faker = Faker()
        data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.first_name()
        }
        return data


class Ingredients:

    ingredients_data = {"ingredients": ["61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa70"]}


