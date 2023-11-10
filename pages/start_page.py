from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StartPage():

    url = "https://eu-north-1.signin.aws.amazon.com/" \
          "oauth?response_type=code&client_id=" \
          "arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&redirect_uri=" \
          "https%3A%2F%2Feu-north-1.console.aws.amazon." \
          "com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26region%3Deu" \
          "-north-1%26state%3DhashArgsFromTB_eu-north-1_4c67827620c13ca7&forceMobileLayout=" \
          "0&forceMobileApp=0&code_challenge=nd7NBn1nwsPoXiHPW2uWNtuqqRacMoF1Yz1NodtfaJM&code_challenge_method=SHA-256"
    user_name = "" #указать свой логин

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    # locators

    aws_signin = "//div[@id='aws-signin-general-user-selection-root']"
    user = "//input[@id='resolving_input']"
    next_button = "//*[@id='next_button']"

    # Getters

    def get_aws_signin(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.aws_signin)))

    def get_user(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user)))

    def get_next_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.next_button)))

    # Actions

    def click_aws_signin(self):
        self.get_aws_signin().click()
        print('Click aws signin')

    def send_user_name(self):
        self.get_user().send_keys(self.user_name)
        print('Send user name')

    def click_next_button(self):
        self.get_next_button().click()
        print('Click next button')

    # Methods

    def go_to_login_page(self):
        self.driver.get(self.url)
        self.click_aws_signin()
        self.send_user_name()
        self.click_next_button()