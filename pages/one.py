from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Try():

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    link = "//a[@href='/']"

    def get_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link)))

    def click_link(self):
        self.get_link().click()
        print('Click link')