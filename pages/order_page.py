import allure
from pages.base_page import BasePage
from locators import locators


class OrderPage(BasePage):


    @allure.step('Получение количества заказов')
    def check_get_counter_order(self, locators):
        return self.get_text_element(locators)

    @allure.step('Получение заказа "В работе"')
    def get_order_list_in_job(self):
        elements = self.get_text_elements(locators.MainFuncConstruct.NUMBER_IN_JOB)
        orders_list = []
        for element in elements:
                order_number = element.text[1:]
                orders_list.append(order_number)
        return orders_list


