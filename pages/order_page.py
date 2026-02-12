import allure
from selenium.common.exceptions import TimeoutException
from locators.locators import MainFuncConstruct
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Ожидаем появления формы 'Лента заказов'")
    def wait_order_feed_visible(self) -> None:
        self.wait_for_element_visible(MainFuncConstruct.ORDER_LENT_FORM)

    @allure.step("Получаем значение счётчика заказов (текст)")
    def get_counter_value(self, locator: tuple[str, str]) -> str:
        element = self.wait_for_element_visible(locator)
        value = element.text.strip().replace(" ", "")
        allure.attach(value, name="Значение счётчика", attachment_type=allure.attachment_type.TEXT)
        return value

    @allure.step("Получаем числовое значение счётчика заказов")
    def check_get_counter_order(self, locator: tuple[str, str]) -> int:
        element = self.wait_for_element_visible(locator)
        text = element.text.strip()
        try:
            return int(text)
        except ValueError:
            allure.attach(self.driver.page_source, "HTML при ошибке", allure.attachment_type.HTML)
            raise AssertionError(f"Ожидалось число, но получено: {text}")

    @allure.step("Получаем список заказов 'В работе'")
    def get_order_list_in_job(self) -> list[str]:
        self.wait_for_elements_visible(MainFuncConstruct.NUMBER_IN_JOB)
        elements = self.driver.find_elements(*MainFuncConstruct.NUMBER_IN_JOB)
        orders = [el.text.strip() for el in elements if el.text.strip()]
        allure.attach(str(orders), name="Список заказов 'В работе'", attachment_type=allure.attachment_type.TEXT)
        return orders

    @allure.step("Ожидание появления конкретного заказа в разделе 'В работе'")
    def wait_order_in_job(self, order_number: str, timeout: int = 15) -> bool:
        try:
            self.wait.until(
                lambda d: any(
                    order_number in el.text
                    for el in d.find_elements(*MainFuncConstruct.NUMBER_IN_JOB)
                )
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидание загрузки ленты заказов")
    def wait_for_orders_feed_loaded(self) -> None:
        self.wait_for_element_visible(MainFuncConstruct.ORDER_LENT_FORM)

