import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage():
    url = "https://eu-north-1.console.aws.amazon.com/console/home?region=eu-north-1#"

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    # locators
    s3 = "//a[contains(text(),'S3')]"


    # Getters

    def get_s3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.s3)))

    # Actions

    def s3_click(self):
        self.get_s3().click()
        print("S3 link click")



