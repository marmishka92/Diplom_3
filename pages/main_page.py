import allure
from seletools.actions import drag_and_drop
from pages.base_page import BasePage
from locators import locators
from locators.main_page_locators import MainPageLocators
from locators.succ_order_modal_locators import SuccessOrderModalLocators


class HeaderPage(BasePage):
    """Шапка сайта — переходы между разделами"""

    @allure.step('Клик по кнопке "Конструктор"')
    def click_to_constructor_btn(self):
        self.click_on_element(locators.MainFuncConstruct.BUTTON_CONSTRUCT)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_to_order_btn(self):
        self.click_on_element(locators.MainFuncConstruct.BUTTON_ORDER_LENT)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_login_btn(self):
        self.click_on_element(locators.MainFuncConstruct.PERS_ACCOUNT)


class MainPage(BasePage):
    """Главная страница конструктора и оформления заказа"""

    @allure.step('Дождаться загрузки главной страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Ожидание появления кнопки "Оформить заказ"')
    def wait_place_order_btn(self):
        self.wait_for_element_visible(MainPageLocators.BUT_ORDER)

    # --- проверки форм ---
    @allure.step('Проверка отображения формы конструктора')
    def check_view_constructor_form(self):
        return self.wait_for_element_visible(locators.MainFuncConstruct.CONSTRUCTOR_FORM)

    @allure.step('Проверка отображения формы ленты заказов')
    def check_view_order_lent_form(self):
        return self.wait_for_element_visible(locators.MainFuncConstruct.ORDER_LENT_FORM)

    # --- работа с ингредиентами ---
    @allure.step('Клик по булке "Краторная N-200i"')
    def click_to_crators_bun(self):
        self.click_on_element(locators.MainFuncConstruct.BUN)

    @allure.step('Проверка появления всплывающего окна ингредиента')
    def check_view_info_ingredient(self):
        return self.wait_for_element_visible(locators.MainFuncConstruct.POP_WINDOW)

    @allure.step('Закрытие всплывающего окна ингредиента крестиком')
    def close_popup_info(self):
        self.click_on_element(locators.MainFuncConstruct.BUTTON_CROSS)

    @allure.step('Проверка, что окно ингредиента закрылось')
    def check_close_popup(self):
        return self.wait_for_element_hide(locators.MainFuncConstruct.POP_WINDOW)

    @allure.step('Добавление булки в корзину')
    def add_bun_cart(self):
        source = self.wait_for_element_visible(locators.MainFuncConstruct.BUN)
        target = self.wait_for_element_visible(locators.MainFuncConstruct.DROP_CONTAINER)
        drag_and_drop(self.driver, source, target)

    @allure.step('Проверка счётчика ингредиента')
    def check_get_info_counter(self):
        return self.get_text_on_element(locators.MainFuncConstruct.COUNTER_INGREDIENT)

    # --- оформление заказа ---
    @allure.step('Создать заказ')
    def create_order(self):
        self.add_bun_cart()
        self.click_on_element(MainPageLocators.BUT_ORDER)

    @allure.step('Проверить, что окно с номером заказа появилось')
    def is_order_success_modal_visible(self):
        return self.wait_for_element_visible(SuccessOrderModalLocators.ORDER_SUCCESS_NUMBER)

    @allure.step('Ожидание завершения анимации оформления заказа')
    def wait_for_animation_end(self):
        self.wait_for_element_hide(SuccessOrderModalLocators.LOADING_ANIMATION)

    @allure.step('Получить номер оформленного заказа')
    def get_number_of_order(self):
        text = self.get_text_on_element(SuccessOrderModalLocators.ORDER_SUCCESS_NUMBER)
        return int(text)

    @allure.step('Закрыть модальное окно успешного заказа')
    def click_close_button_success_modal(self):
        self.click_on_element(SuccessOrderModalLocators.BUTTON_CLOSE_MODAL_ORDER)

    @allure.step('Ожидание скрытия модального окна заказа')
    def wait_for_order_success_modal_hidden(self):
        self.wait_for_element_hide(SuccessOrderModalLocators.ORDER_SUCCESS_NUMBER)

    # --- переходы по ссылкам ---
    @allure.step('Переход по ссылке "Лента заказов"')
    def click_by_link_orders_feed(self):
        self.click_on_element(MainPageLocators.LINK_ORDER_FEED)

    @allure.step('Переход по ссылке "Конструктор"')
    def click_by_link_constructor(self):
        self.click_on_element(MainPageLocators.LINK_CONSTRUCT)
