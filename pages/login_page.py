import allure
from pages.base_page import BasePage
from locators import locators


class LoginPage(BasePage):


    @allure.step('Проверка отображения формы авторизации')
    def check_auth_form(self):
        return self.check_element(locators.AccountLogin.FORM_AUTH)

    @allure.step('Заполнение поля email')
    def send_field_email(self, email):
        self.send_to_field(locators.AccountLogin.EMAIL_AUTH, email)

    @allure.step('Заполнение поля password')
    def send_field_password(self, password):
        self.send_to_field(locators.AccountLogin.PASS_AUTH, password)

    @allure.step('Клик на кнопку Войти в аккаунт')
    def click_login_btn(self):
        self.move_to_element_click(locators.AccountLogin.BUTTON_ENTER)

    @allure.step('Авторизация на сайте')
    def login_auth(self, email, password):
        self.send_field_email(email)
        self.send_field_password(password)
        self.click_login_btn()

    @allure.step('Ожидание невидимых окон в Firefox')
    def not_vision_window(self):
        self.wait_element_not_vision(locators.NotVisionPopup.WINDOW_1)
        self.wait_element_not_vision(locators.NotVisionPopup.WINDOW_2)
        self.wait_element_not_vision(locators.NotVisionPopup.WINDOW_3)

