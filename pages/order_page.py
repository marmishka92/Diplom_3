import allure
from pages.base_page import BasePage
from locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from SuccessOrderModalLocators import SuccessOrderModalLocators


class OrderPage(BasePage):

    @allure.step('Получение количества заказов (текст)')
    def check_get_counter_order2(self, locators):
        return self.get_text_element(locators)

    @allure.step("Получаем числовое значение счётчика заказов")
    def check_get_counter_order(self, locator):
        """Ожидаем обновления счётчика на странице заказов"""
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator)
        )
        text = element.text.strip()
        try:
            return int(text)
        except ValueError:
            allure.attach(self.driver.page_source, "HTML при ошибке", allure.attachment_type.HTML)
            raise AssertionError(f"Ожидалось число, но получено: {text}")

    @allure.step('Получение списка заказов "В работе"')
    def get_order_list_in_job(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_all_elements_located(locators.MainFuncConstruct.NUMBER_IN_JOB)
        )
        elements = self.driver.find_elements(*locators.MainFuncConstruct.NUMBER_IN_JOB)
        orders = [el.text.strip() for el in elements if el.text.strip()]
        allure.attach(str(orders), name="Список заказов 'В работе'", attachment_type=allure.attachment_type.TEXT)
        return orders

    @allure.step('Ожидание появления конкретного заказа в разделе "В работе"')
    def wait_order_in_job(self, order_number: str, timeout: int = 15):
        """Ожидает появления конкретного номера заказа без time.sleep"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: any(
                    order_number in el.text
                    for el in d.find_elements(*locators.MainFuncConstruct.NUMBER_IN_JOB)
                )
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидание загрузки ленты заказов")
    def wait_for_orders_feed_loaded(self):
        """Ждём, пока появится блок ленты заказов."""
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(locators.MainFuncConstruct.ORDER_LENT_FORM)
        )

    @allure.step("Получаем значение счётчика заказов (текст)")
    def get_counter_value(self, locator):
        """Возвращает текстовое значение счётчика"""
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(locator)
        )
        value = element.text.strip().replace(" ", "")
        allure.attach(value, name="Значение счётчика", attachment_type=allure.attachment_type.TEXT)
        return value

