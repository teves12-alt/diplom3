import pytest
import allure
import requests
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from data import BASE_URL, REGISTER_URL, LOGIN_URL, DELETE_USER_URL


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """Инициализация драйвера для Chrome и Firefox."""
    browser_name = request.param

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        browser = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser_name}")

    browser.get(BASE_URL)
    yield browser
    browser.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)


@pytest.fixture(scope="function")
def auth_user(driver):
    """Создаёт пользователя через API, логинит через UI, удаляет после теста."""
    import random
    import string

    email = f"test_{''.join(random.choices(string.ascii_lowercase, k=6))}@yandex.ru"
    password = "password123"
    name = "Тестовый Пользователь"

    # Регистрация через API
    resp = requests.post(REGISTER_URL, json={
        "email": email,
        "password": password,
        "name": name,
    })
    token = resp.json()["accessToken"]

    # Логин через UI
    login_page = LoginPage(driver)
    login_page.login(email, password)

    yield {"email": email, "password": password, "name": name, "token": token}

    # Очистка через API
    requests.delete(DELETE_USER_URL, headers={"Authorization": token})
