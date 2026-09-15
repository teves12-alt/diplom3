from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы (Конструктор)."""

    # Кнопки навигации в хедере
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")

    # Кнопка «Войти в аккаунт» (для неавторизованного пользователя)
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Кнопка «Оформить заказ» (для авторизованного пользователя)
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Вкладки конструктора
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")

    # Активная вкладка
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")

    # Ингредиенты в конструкторе
    INGREDIENT_CARD = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient__')]")
    INGREDIENT_NAME = (By.XPATH, ".//p[@class='undefined text_type_main_default']")

    # Модальное окно ингредиента
    INGREDIENT_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal__')]")
    INGREDIENT_MODAL_TITLE = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal__')]//h2"
    )
    INGREDIENT_MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal__')]//button[contains(@class, 'modal__close')]"
    )

    # Счётчик ингредиента
    INGREDIENT_COUNTER = (
        By.XPATH,
        "//div[contains(@class, 'BurgerIngredient_ingredient__')]//div[contains(@class, 'counter_counter__')]"
    )

    # Корзина (зона переноса ингредиентов)
    CONSTRUCTOR_BASKET = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_constructor__')]")

    # Номер заказа в модалке после оформления
    ORDER_NUMBER_MODAL = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal__')]//p[contains(@class, 'text_type_digits-large')]"
    )
