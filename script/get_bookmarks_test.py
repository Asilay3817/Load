from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.start_page import StartPage
from pages.login_page import LoginPage
from pages.one import Try
from pages.main_page import MainPage
from pages.buckets_page import BucketsPage
from pages.search_page import SearchPage
from service.transfer import Transfer

def test_load_bookmarks():
    from selenium.webdriver.chrome.options import Options

    # поменять на свой путь (папка с этим проектом, найти в папке файл chromedriver - скопировать его путь и заменить значение в кавычках)
    service = Service(executable_path = '/Users/asilay/Desktop/study/QA/Loader/chromedriver')
    o = Options()

    # в download.default_directory указать свой путь к папке куда будут сохраняться букмарки, такой же как для скрипта transfer

    prefs = {
        "download.default_directory": "/Users/asilay/Desktop/bm/",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    o.add_experimental_option("prefs", prefs)
    o.add_argument("--detach")
    # o.add_experimental_option("detach", True)
    o.add_argument("--headless")
    o.add_argument("--window-size=1800,900")
    driver = webdriver.Chrome(service=service, options=o)
    # driver.maximize_window()

    sp = StartPage(driver)
    sp.go_to_login_page()

    lp = LoginPage(driver)
    lp.sign_in()

    one = Try(driver)
    one.click_link()

    mp = MainPage(driver)
    mp.s3_click()

    bp = BucketsPage(driver)
    bp.click_nogeo()

    sp = SearchPage(driver)
    sp.send_id()
    sp.find_all()
    sp.find_and_download()

    tr = Transfer(driver)
    tr.change_format()

    driver.close()
    driver.quit()
