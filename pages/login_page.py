from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():

    account_id = "" #по желанию можно заменить на свой id
    user_name = "" #указать свой логин
    password = "" #указать свой пароль

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    # locators

    id_field = "//input[@id='account']"
    user_name_field = "//input[@id='username']"
    password_field = "//input[@id='password']"
    login_button = "//a[@id='signin_button']"

    # Getters

    def get_id_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.id_field)))

    def get_user_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    # Actions

    def send_id(self):
        self.get_id_field().send_keys(self.account_id)
        print('Send id')

    def send_name(self):
        self.get_user_name_field().send_keys(self.user_name)
        print('Send name')

    def send_password(self):
        self.get_password_field().send_keys(self.password)
        print('Send password')

    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')

    # Methods

    def sign_in(self):
        self.send_id()
        self.send_name()
        self.send_password()
        self.click_login_button()
