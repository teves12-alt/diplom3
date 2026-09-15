import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data import BASE_URL


class LoginPage(BasePage):
    """Page Object страницы авторизации."""

    @allure.step("Открываем страницу логина")
    def open(self):
        self.driver.get(f"{BASE_URL}/login")

    @allure.step("Вводим email")
    def enter_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step("Вводим пароль")
    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step("Кликаем кнопку «Войти»")
    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Логинимся под пользователем")
    def login(self, email, password):
        self.open()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
