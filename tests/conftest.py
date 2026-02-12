import pytest
import requests
from selenium import webdriver
from faker import Faker
from urls import UrlsApi
from data import RegUser
from pages.login_page import LoginPage
from pages.main_page import HeaderPage, MainPage
from pages.base_page import BasePage
from seletools.actions import drag_and_drop


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    driver.get(UrlsApi.MAIN)
    if request.param == 'firefox':
        try:
            LoginPage(driver).not_vision_window()
        except Exception:
            pass
    yield driver
    driver.quit()


@pytest.fixture
def create_user():
    faker = Faker()
    payload = RegUser.create_user_new()
    unique_suffix = faker.random_int(1000, 9999)
    payload["email"] = payload["email"].replace("@", f"+{unique_suffix}@")
    response = requests.post(UrlsApi.REG_USER, json=payload)
    if response.status_code != 200 or "accessToken" not in response.json():
        pytest.skip(f"Ошибка регистрации: {response.status_code}, {response.text}")
    token = response.json()["accessToken"]
    yield payload, response
    try:
        requests.delete(UrlsApi.DEL_USER, headers={"Authorization": token})
    except Exception:
        pass


@pytest.fixture()
def login(driver, create_user):
    data = create_user[0]
    HeaderPage(driver).click_login_btn()
    LoginPage(driver).login_auth(data["email"], data["password"])
    MainPage(driver).main_page_loading_wait()

