import allure
from data import UrlsApi
from pages.main_page import HeaderPage, MainPage


class TestMainPage:

    @allure.title('Проверка перехода кликом на "Конструктор"')
    def test_click_constructor_btn(self, driver):
        header = HeaderPage(driver)
        main_page = MainPage(driver)
        header.click_login_btn()
        header.click_to_constructor_btn()
        assert main_page.get_current_url().rstrip("/") == UrlsApi.MAIN.rstrip("/")
        assert main_page.check_view_constructor_form()

    @allure.title('Проверка перехода кликом на "Лента Заказов"')
    def test_click_lent_order(self, driver):
        header = HeaderPage(driver)
        main_page = MainPage(driver)
        header.click_login_btn()
        header.click_to_order_btn()
        assert main_page.get_current_url() == UrlsApi.ORDER_LENT
        assert main_page.check_view_order_lent_form()

    @allure.title('Проверка появления информации об ингредиенте')
    def test_popup_info_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_crators_bun()
        assert main_page.check_view_info_ingredient()

    @allure.title('Проверка закрытия всплывающего окна крестиком')
    def test_close_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_crators_bun()
        main_page.close_popup_info()
        assert main_page.check_close_popup()

    @allure.title('Проверка счетчика ингредиентов')
    def test_counter_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.add_bun_cart()
        assert int(main_page.check_get_info_counter()) == 2
