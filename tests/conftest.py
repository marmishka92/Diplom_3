import pytest
import requests
from selenium import webdriver
from data import UrlsApi, RegUser
from pages.login_page import LoginPage
from pages.main_page import HeaderPage, MainPage


@pytest.fixture(params= ['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
       driver = webdriver.Chrome()
       driver.set_window_size(1920, 1080)
       driver.get(UrlsApi.MAIN)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(UrlsApi.MAIN)
        not_vision = LoginPage(driver)
        not_vision.not_vision_window()
    yield driver
    driver.quit()


@pytest.fixture
def create_user():
    payload = RegUser.create_user_new()
    response = requests.post(UrlsApi.REG_USER, data=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(UrlsApi.DEL_USER, headers={"Authorization": token})


@pytest.fixture()
def login(driver, create_user):
        create_data_user = create_user[0]
        head_page = HeaderPage(driver)
        login_page = LoginPage(driver)
        head_page.click_login_btn()
        login_page.login_auth(create_data_user["email"], create_data_user["password"])
        main_page = MainPage(driver)
        main_page.wait_place_order_btn()



