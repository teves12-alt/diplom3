import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import BASE_URL


class MainPage(BasePage):
    """Page Object главной страницы (Конструктор)."""

    @allure.step("Открываем главную страницу")
    def open(self):
        self.driver.get(BASE_URL)

    @allure.step("Кликаем «Конструктор»")
    def click_constructor_button(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликаем «Лента заказов»")
    def click_order_feed_button(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликаем на первый ингредиент")
    def click_first_ingredient(self):
        self.click(MainPageLocators.INGREDIENT_CARD)

    @allure.step("Проверяем, открыто ли модальное окно ингредиента")
    def is_ingredient_modal_open(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL)

    @allure.step("Получаем заголовок модального окна ингредиента")
    def get_ingredient_modal_title(self):
        return self.get_text(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step("Закрываем модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click(MainPageLocators.INGREDIENT_MODAL_CLOSE_BUTTON)

    @allure.step("Ожидаем закрытия модального окна")
    def wait_ingredient_modal_closed(self):
        self.wait_for_element_to_disappear(MainPageLocators.INGREDIENT_MODAL)

    @allure.step("Получаем значение счётчика первого ингредиента")
    def get_first_ingredient_counter(self):
        try:
            return int(self.get_text(MainPageLocators.INGREDIENT_COUNTER))
        except Exception:
            return 0

    @allure.step("Добавляем первый ингредиент в заказ (drag-and-drop)")
    def add_ingredient_to_order(self):
        from selenium.webdriver import ActionChains

        ingredient = self.wait_for_element(MainPageLocators.INGREDIENT_CARD)
        basket = self.wait_for_element(MainPageLocators.CONSTRUCTOR_BASKET)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, basket).perform()

    @allure.step("Кликаем «Оформить заказ»")
    def click_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    @allure.step("Получаем номер заказа из модального окна")
    def get_order_number_from_modal(self):
        return self.get_text(MainPageLocators.ORDER_NUMBER_MODAL)

    @allure.step("Проверяем, видна ли кнопка «Оформить заказ»")
    def is_order_button_visible(self):
        return self.is_element_visible(MainPageLocators.ORDER_BUTTON)
