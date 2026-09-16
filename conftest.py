import pytest
from selenium import webdriver

from helpers import generate_user_data, register_user, login_user, delete_user
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)


@pytest.fixture
def user_data():
    return generate_user_data()


@pytest.fixture
def auth_user(driver, login_page, user_data):
    register_user(user_data)
    login_page.open()
    login_page.login(user_data["email"], user_data["password"])

    login_response = login_user({
        "email": user_data["email"],
        "password": user_data["password"],
    })
    token = login_response.json()["accessToken"]
    user_data["token"] = token

    yield user_data

    delete_user({"Authorization": token})


    # Очистка через API
    requests.delete(DELETE_USER_URL, headers={"Authorization": token})
