import requests
import allure
from urls import UrlsApi
from data import Ingredients


class Order:

    @allure.step('Создание нового заказа пользователя через API')
    def create_order(self, create_user):
        """Создаёт заказ, если у пользователя есть токен"""
        response = create_user[1]
        try:
            token = response.json().get("accessToken")
        except Exception:
            allure.attach(str(response.text), "Ошибка при получении токена", allure.attachment_type.TEXT)
            raise AssertionError("Не удалось получить accessToken при создании заказа")

        if not token:
            raise AssertionError(f"Токен отсутствует, ответ сервера: {response.text}")

        headers = {"Authorization": token}
        response_order = requests.post(
            UrlsApi.CREATE_ORDER,
            headers=headers,
            json=Ingredients.ingredients_data  # ✅ исправлено
        )

        allure.attach(response_order.text, "Ответ при создании заказа", allure.attachment_type.TEXT)
        assert response_order.status_code == 200, f"Ошибка создания заказа: {response_order.text}"
        return response_order.json()

    @allure.step('Получение заказов пользователя через API')
    def get_user_orders(self, create_user):
        """Возвращает номер первого заказа пользователя"""
        response = create_user[1]
        token = response.json().get("accessToken")

        if not token:
            raise AssertionError("Отсутствует accessToken, пользователь не авторизован")

        headers = {"Authorization": token}
        response_orders = requests.get(UrlsApi.GET_ORDER_USER, headers=headers)

        allure.attach(response_orders.text, "Ответ при получении заказов", allure.attachment_type.TEXT)
        assert response_orders.status_code == 200, f"Ошибка получения заказов: {response_orders.text}"

        orders = response_orders.json().get("orders", [])
        if not orders:
            raise AssertionError("Список заказов пуст")

        return orders[0]["number"]
