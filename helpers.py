import requests
import allure
from data import UrlsApi, Ingredients


class Order:


    @allure.step('Создание нового заказа пользователя через API')
    def create_order(self, create_user):
        token = create_user[1].json()["accessToken"]
        headers = {'Authorization': token}
        requests.post(UrlsApi.CREATE_ORDER, headers=headers, data=Ingredients.ingredients_data)

    @allure.step('Получение заказов пользователя через API')
    def get_user_orders(self, create_user):
        token = create_user[1].json()["accessToken"]
        headers = {'Authorization': token}
        response = requests.get(UrlsApi.GET_ORDER_USER, headers=headers)
        return response.json()["orders"][0]["number"]

