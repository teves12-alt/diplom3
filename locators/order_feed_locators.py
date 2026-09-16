from selenium.webdriver.common.by import By


class OrderFeedLocators:
    """Локаторы страницы Ленты заказов."""

    # Счётчик «Выполнено за всё время»
    TOTAL_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за всё время']/following-sibling::p[contains(@class, 'text_type_digits-large')]"
    )

    # Счётчик «Выполнено за сегодня»
    TODAY_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня']/following-sibling::p[contains(@class, 'text_type_digits-large')]"
    )

    # Раздел «В работе»
    IN_PROGRESS_SECTION = (By.XPATH, "//p[text()='В работе']")

    # Номера заказов в разделе «В работе»
    IN_PROGRESS_ORDER_NUMBERS = (
        By.XPATH,
        "//p[text()='В работе']/following::ul[contains(@class, 'OrderFeed_orderList__')]//li"
    )
