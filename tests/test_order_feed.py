import allure
import requests
from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from data import ORDERS_URL, INGREDIENTS_URL


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("При создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_total_counter_increases(self, order_feed_page, auth_user):
        order_feed_page.open()
        initial_total = order_feed_page.get_total_counter()

        token = auth_user["token"]
        ingredients_resp = requests.get(INGREDIENTS_URL)
        ingredient_ids = [item["_id"] for item in ingredients_resp.json()["data"][:2]]

        order_resp = requests.post(
            ORDERS_URL,
            json={"ingredients": ingredient_ids},
            headers={"Authorization": token},
        )
        assert order_resp.status_code == 200

        order_feed_page.open()
        new_total = order_feed_page.get_total_counter()

        assert new_total > initial_total, (
            f"Счётчик «Выполнено за всё время» не увеличился: "
            f"было {initial_total}, стало {new_total}"
        )

    @allure.title("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_counter_increases(self, order_feed_page, auth_user):
        order_feed_page.open()
        initial_today = order_feed_page.get_today_counter()

        token = auth_user["token"]
        ingredients_resp = requests.get(INGREDIENTS_URL)
        ingredient_ids = [item["_id"] for item in ingredients_resp.json()["data"][:2]]

        order_resp = requests.post(
            ORDERS_URL,
            json={"ingredients": ingredient_ids},
            headers={"Authorization": token},
        )
        assert order_resp.status_code == 200

        order_feed_page.open()
        new_today = order_feed_page.get_today_counter()

        assert new_today > initial_today, (
            f"Счётчик «Выполнено за сегодня» не увеличился: "
            f"было {initial_today}, стало {new_today}"
        )

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_appears_in_progress(self, order_feed_page, auth_user):
        token = auth_user["token"]
        ingredients_resp = requests.get(INGREDIENTS_URL)
        ingredient_ids = [item["_id"] for item in ingredients_resp.json()["data"][:2]]

        order_resp = requests.post(
            ORDERS_URL,
            json={"ingredients": ingredient_ids},
            headers={"Authorization": token},
        )
        order_number = str(order_resp.json()["order"]["number"])

        order_feed_page.open()
        in_progress_orders = order_feed_page.get_in_progress_order_numbers()

        assert order_number in in_progress_orders, (
            f"Номер заказа {order_number} не найден в разделе «В работе». "
            f"Текущие заказы в работе: {in_progress_orders}"
        )

