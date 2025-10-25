import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # Поиск элемента с ожиданием
    def find_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    # Ожидание кликабельности элемента
    def wait_element_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    # Ожидание загрузки элемента
    def wait_element_load(self, locator):
        WebDriverWait(self.driver, 90).until(EC.visibility_of_element_located(locator))

    # Клик на кнопку
    def click_button(self, locator):
        self.wait_element_clickable(locator)
        self.driver.find_element(*locator).click()

    # Получение url
    def get_current_url(self):
        return self.driver.current_url

    # Заполнить поле
    def send_to_field(self, locator, text):
        self.wait_element_load(locator)
        self.driver.find_element(*locator).send_keys(text)

    # Получить текст элементов
    def get_text_elements(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    # Получить текст элемента
    def get_text_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    # Проверка отображения элемента
    def check_element(self, locator):
        self.wait_element_load(locator)
        return self.driver.find_element(*locator)

    # Проверка отображения невидимого элемента
    def check_element_not_vision(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # Перетаскивание элемента
    def drag_and_drop(self, element_one, element_two):
        element = self.driver.find_element(*element_one)
        target = self.driver.find_element(*element_two)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()

    # Переход к элементу и клик на него
    def move_to_element_click(self, locator):
        element = self.driver.find_element(*locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()

    # Ожидание невидимого элемента
    def wait_element_not_vision(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))





