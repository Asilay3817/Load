import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage():

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    # locators
    s3 = "//a[@id='link-self:r53:']"


    # Getters

    def get_s3(self):
        return WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, self.s3)))

    # Actions
    # def find_s3(self):
    #     href = "https://s3.console.aws.amazon.com/s3/home?"
    #     time.sleep(1)
    #     nested_elements = self.driver.find_elements(By.XPATH, "//a[@href]")  # получаем все элемнеты содержащие данный xpath
    #     found_other_elements = filter(lambda e: href in e.get_attribute('href'), nested_elements)  # сортируем элементы по заданному соответствию
    #     elements_list = list(found_other_elements)
    #     print(len(elements_list))
    #
    #     for i in elements_list:
    #         if i.get_attribute('href'):
    #             i.click()

    def s3_click(self):
        self.get_s3().click()
        print("S3 link click")

