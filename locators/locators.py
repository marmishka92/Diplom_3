import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class AccountLogin:

    FORM_AUTH = [By.XPATH, ".//div[@class='Auth_login__3hAey']"] # Форма авторизации
    BUTTON_LOGIN = [By.XPATH, ".//button[text()='Войти в аккаунт']"] # Кнопка Войти в Аккаунт
    EMAIL_AUTH = [By.XPATH, ".//label[text()='Email']/following-sibling::input"] # Поле Email в форме авторизации
    PASS_AUTH = [By.XPATH, ".//input[@name='Пароль']"]# Поле Пароль в форме авторизации
    BUTTON_ENTER = [By.XPATH, ".//button[text()='Войти']"] # Кнопка Войти в форме авторизации
    BUTTON_ENTER_REG = [By.XPATH, ".//a[text()='Войти']"] # Кнопка войти в форме регистрации
    BUTTON_ENTER_FORGOT = [By.XPATH, ".//p/a[text()='Войти']"] # Кнопка Войти в форме восстановить пароль


class MainFuncConstruct:


    BUTTON_CONSTRUCT = [By.XPATH, ".//p[text()= 'Конструктор']"] # Кнопка Конструктор в хедере
    BUTTON_ORDER_LENT = [By.XPATH, ".//p[text()= 'Лента Заказов']"] # Кнопка Лента Заказов
    BUN = [By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']"] # Ингредиент булка
    INGREDIENT_SAUCE =[By.XPATH, ".//img[@alt='Соус фирменный Space Sauce']"] # Ингредиент Соус
    INGREDIENT_FILLING = [By.XPATH, ".//img[@alt='Мясо бессмертных моллюсков Protostomia']"] # Ингредиент Начинка
    POP_WINDOW = [By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']"] # Всплывающее окно
    BUTTON_CROSS = [By.XPATH, ".//button[@type='button'][1]"] # Кнопка крестик
    COUNTER_INGREDIENT = [By.XPATH, ".//p[@class='counter_counter__num__3nue1']"] # Счетчик кол-ва ингредиента в заказе
    COUNTER_ALL_TIME = [By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p"] # Счетчик заказов за всё время
    COUNTER_TODAY = [By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p"] # Счетчик за сегодня
    PERS_ACCOUNT = [By.XPATH, ".//a/p[text()='Личный Кабинет']"] # Кнопка "Личный кабинет"
    CONSTRUCTOR_FORM = [By.XPATH, ".//div[@class ='BurgerIngredients_ingredients__menuContainer__Xu3Mo']"] # Форма конструктора
    ORDER_LENT_FORM = [By.XPATH, ".//div[@class ='OrderFeed_orderFeed__2RO_j']"] # Форма Лента заказов
    CART = [By.XPATH, ".//div[@class='constructor-element constructor-element_pos_top']"] # Корзина
    DROP_CONTAINER = [By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]"] #Область перетаскивания
    PLACE_ORDER = [By.XPATH, ".//button[text()='Оформить заказ']"]  # Кнопка Оформить заказ
    FORM_ORDER = [By.XPATH, ".//div[@class = 'Modal_modal__container__Wo2l_']"] # Форма заказа
    NUMBER_ORDER = [By.XPATH, ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"] # Номер заказа
    NUMBER_IN_JOB = [By.XPATH, ".//li[@class='text text_type_digits-default mb-2']"] # Номер заказа в работе
    ORDER_HISTORY = [By.XPATH, ".//p[@class='text_type_digits-default']"] # История заказов
    BUTTON_CROSS_IN_ORDER = [By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"] # Крестик в окне с закказом


class NotVisionPopup:

    WINDOW_1 = [By.XPATH, ".//div[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"]
    WINDOW_2 = [By.XPATH, ".//section[@class='Modal_modal__P3_V5']/div[@class='Modal_modal_overlay__x2ZCr']"]
    WINDOW_3 = [By.XPATH, ".//div[@class='Modal_modal__P3_V5']/div[@class='Modal_modal_overlay__x2ZCr']"]