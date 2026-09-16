import allure
from pages.main_page import MainPage


@allure.feature("Основной функционал — Конструктор")
class TestMainPage:

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, main_page, login_page, auth_user):
        main_page.click_constructor_button()
        assert main_page.is_order_button_visible(), "Кнопка «Оформить заказ» не видна"

    @allure.title("Переход по клику на «Лента заказов»")
    def test_go_to_order_feed(self, main_page):
        main_page.click_order_feed_button()
        assert "/feed" in main_page.get_current_url(), "Не произошёл переход на ленту заказов"

    @allure.title("При клике на ингредиент появляется всплывающее окно с деталями")
    def test_ingredient_modal_opens(self, main_page):
        main_page.open()
        main_page.click_first_ingredient()
        assert main_page.is_ingredient_modal_open(), "Модальное окно ингредиента не открылось"

    @allure.title("В модальном окне ингредиента есть заголовок")
    def test_ingredient_modal_has_title(self, main_page):
        main_page.open()
        main_page.click_first_ingredient()
        title = main_page.get_ingredient_modal_title()
        assert title, "Заголовок модального окна пустой"

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_ingredient_modal_closes(self, main_page):
        main_page.open()
        main_page.click_first_ingredient()
        main_page.close_ingredient_modal()
        main_page.wait_ingredient_modal_closed()
        assert not main_page.is_ingredient_modal_open(), "Модальное окно не закрылось"

    @allure.title("При добавлении ингредиента в заказ счётчик увеличивается")
    def test_ingredient_counter_increases(self, main_page):
        main_page.open()
        initial_counter = main_page.get_first_ingredient_counter()
        main_page.add_ingredient_to_order()
        new_counter = main_page.get_first_ingredient_counter()
        assert new_counter > initial_counter, (
            f"Счётчик не увеличился: было {initial_counter}, стало {new_counter}"
        )
