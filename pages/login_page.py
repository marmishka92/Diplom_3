import allure
from pages.base_page import BasePage
from locators import locators


class LoginPage(BasePage):
    """Страница авторизации"""

    @allure.step('Проверка отображения формы авторизации')
    def check_auth_form(self):
        return self.check_element(locators.AccountLogin.FORM_AUTH)

    @allure.step('Заполнение поля Email')
    def send_field_email(self, email):
        self.send_to_field(locators.AccountLogin.EMAIL_AUTH, email)

    @allure.step('Заполнение поля Password')
    def send_field_password(self, password):
        self.send_to_field(locators.AccountLogin.PASS_AUTH, password)

    @allure.step('Клик по кнопке "Войти"')
    def click_login_btn(self):
        self.move_to_element_click(locators.AccountLogin.BUTTON_ENTER)

    @allure.step('Авторизация на сайте')
    def login_auth(self, email, password):
        """Основной сценарий логина"""
        self.send_field_email(email)
        self.send_field_password(password)
        self.click_login_btn()

    @allure.step('Регистрация нового пользователя через UI')
    def register_user_ui(self, name, email, password):
        self.click_on_element(locators.BUTTON_REGISTER)
        self.send_to_field(locators.INPUT_NAME, name)
        self.send_to_field(locators.INPUT_EMAIL, email)
        self.send_to_field(locators.INPUT_PASSWORD, password)
        self.click_on_element(locators.BUTTON_SUBMIT)

    @allure.step('Ожидание закрытия всплывающих окон')
    def not_vision_window(self):
        """Используется в Firefox — ожидаем, пока закроются все окна."""
        self.wait_element_not_vision(locators.NotVisionPopup.WINDOW_1)
        self.wait_element_not_vision(locators.NotVisionPopup.WINDOW_2)
        self.wait_element_not_vision(locators.NotVisionPopup.WINDOW_3)
