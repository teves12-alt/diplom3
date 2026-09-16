import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from urls import BASE_URL


class OrderFeedPage(BasePage):
    """Page Object страницы Ленты заказов."""

    @allure.step("Открываем ленту заказов")
    def open(self):
        self.open_url(f"{BASE_URL}/feed")

    @allure.step("Получаем значение счётчика «Выполнено за всё время»")
    def get_total_counter(self):
        return int(self.get_text(OrderFeedLocators.TOTAL_COUNTER))

    @allure.step("Получаем значение счётчика «Выполнено за сегодня»")
    def get_today_counter(self):
        return int(self.get_text(OrderFeedLocators.TODAY_COUNTER))

    @allure.step("Получаем список номеров заказов в разделе «В работе»")
    def get_in_progress_order_numbers(self):
        elements = self.find_elements(OrderFeedLocators.IN_PROGRESS_ORDER_NUMBERS)
        return [el.text for el in elements if el.text.strip()]

