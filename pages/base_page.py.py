import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех Page Object."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Ожидаем видимости элемента: {locator}")
    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидаем кликабельности элемента: {locator}")
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Кликаем по элементу: {locator}")
    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    @allure.step("Вводим текст в поле: {locator}")
    def send_keys(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получаем текст элемента: {locator}")
    def get_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step("Проверяем, что элемент виден: {locator}")
    def is_element_visible(self, locator):
        try:
            self.wait_for_element(locator)
            return True
        except Exception:
            return False

    @allure.step("Ожидаем, что элемент исчезнет: {locator}")
    def wait_for_element_to_disappear(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидаем перехода на URL, содержащий: {url_fragment}")
    def wait_for_url(self, url_fragment):
        return self.wait.until(EC.url_contains(url_fragment))
