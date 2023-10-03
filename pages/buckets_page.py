from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BucketsPage():

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    # locators

    nogeo = "//a[@href='/s3/buckets/mapsme-bookmarks-private-nogeo?region=eu-north-1']"


    # Getters

    def get_nogeo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.nogeo)))

    # Actions

    def click_nogeo(self):
        self.get_nogeo().click()
        print('Click nogeo')

