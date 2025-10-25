import pytest
import allure
import helpers
from helpers import Order
from locators import locators
from pages.main_page import HeaderPage
from pages.order_page import OrderPage


class TestOrderPage:


    @pytest.mark.parametrize('counter', [locators.MainFuncConstruct.COUNTER_TODAY, locators.MainFuncConstruct.COUNTER_ALL_TIME])
    @allure.title('Проверка увеличения счетчика "Выполнено за всё время" и "Выполнено за сегодня"')
    def test_counter_all_time_and_today(self, driver, create_user, login, counter):
        order_page = OrderPage(driver)
        order = Order()
        headers = HeaderPage(driver)
        headers.click_to_order_btn()
        counter_old = int(order_page.check_get_counter_order(counter))
        order.create_order(create_user)
        new_counter = int(order_page.check_get_counter_order(counter))
        assert new_counter > counter_old


    @allure.title('Проверка появления заказа в разделе "В работе"')
    def test_get_number_in_job(self, driver, create_user, login):
        order = Order()
        order_page = OrderPage(driver)
        headers = HeaderPage(driver)
        headers.click_to_order_btn()
        order.create_order(create_user)
        in_job = order_page.get_order_list_in_job()
        list_order = str(helpers.Order.get_user_orders(self, create_user))
        assert list_order in in_job



