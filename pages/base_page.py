from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # ===== Базовые ожидания / действия =====
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_hide(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def click_on_element(self, locator):
        self.wait_for_element_clickable(locator).click()

    def send_to_field(self, locator, text):
        el = self.wait_for_element_visible(locator)
        el.clear()
        el.send_keys(text)

    def get_text_on_element(self, locator):
        return self.wait_for_element_visible(locator).text.strip()

    def move_to_element_click(self, locator):
        el = self.wait_for_element_visible(locator)
        ActionChains(self.driver).move_to_element(el).click().perform()

    def drag_and_drop_element(self, source, target):
        # source / target — уже найденные элементы (см. вызов в MainPage)
        drag_and_drop(self.driver, source, target)

    def wait_for_attribute(self, locator, attribute, value):
        return self.wait.until(EC.text_to_be_present_in_element_attribute(locator, attribute, value))

    def get_current_url(self):
        return self.driver.current_url

    # ===== Вспомогательные (нужны LoginPage и проверки видимости) =====
    def check_element(self, locator):
        """True, если элемент видим (для 'check_auth_form')."""
        try:
            self.wait_for_element_visible(locator)
            return True
        except Exception:
            return False

    def wait_element_not_vision(self, locator):
        """Алиас под существующий вызов в LoginPage.not_vision_window()."""
        return self.wait_for_element_hide(locator)

