import time
import datetime
import os

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



class SearchPage():

    your_input = input("Введите user_id: ")

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    # locators
    search_field = "//input[@aria-label='Find objects by prefix']"
    folders = "//span[@class='name folder latest object-name']"

    # Getters
    def get_search_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field)))

    def get_folders(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.folders)))

    # Actions
    def send_id(self):
        self.get_search_field().send_keys(self.your_input)
        self.get_search_field().send_keys(Keys.RETURN)
        print('Send user_id')

    # Methods
    def find_all(self):
        time.sleep(1)
        elements = self.driver.find_elements(By.XPATH, "//a[@href]") # получаем все элемнеты содержащие данный xpath
        return elements

    def find_and_download(self):

        selected_elements = []
        selected_elements_2 = []

        href = "/s3/buckets/mapsme-bookmarks-private-nogeo?"

        found_elements = filter(lambda e: href in e.get_attribute('href'), self.find_all()) # сортируем элементы по заданному соответствию
        filtered_elements_list = list(found_elements)

        # переносим все ссылки на начальные папки в отдельный список
        for element in filtered_elements_list:
            if element.get_attribute('href'):
                link = element.get_attribute('href')
                selected_elements.append(link)

        # перебираем список начальных папок открывая их, сохраняем ссылки на все вложенные папки
        for i in selected_elements:
            self.driver.get(i)
            print("Open ID folder")
            # self.driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(1)
            nested_elements = self.driver.find_elements(By.XPATH, "//a[@href]") # получаем все элемнеты содержащие данный xpath
            found_other_elements = filter(lambda e: href in e.get_attribute('href'), nested_elements) # сортируем элементы по заданному соответствию
            elements_list = list(found_other_elements)

            # переносим все ссылки на вложенные папки в отдельный список
            for b in elements_list:
                link = b.get_attribute('href')
                selected_elements_2.append(link)

            # перебираем список вложенных папок открывая их, сохраняем ссылки на конечные папки
            for other_element in selected_elements_2:
                time.sleep(1)
                self.driver.get(other_element)
                print("Open device folder")
                time.sleep(1)
                last_elements = self.driver.find_elements(By.XPATH, "//a[@href]")  # получаем все элемнеты содержащие данный xpath
                found_last_elements = filter(lambda e: "/s3/buckets/mapsme-bookmarks-private-nogeo?region=" in e.get_attribute('href'), last_elements)  # сортируем
                last_elements_list = list(found_last_elements)
                endpoint_list = []

                for elem in last_elements_list:
                    link = elem.get_attribute('href')
                    endpoint_list.append(link)

                # проходим по списку из конечных папок
                for c in endpoint_list:
                    time.sleep(1)
                    self.driver.get(c)
                    print("Open the folder with bookmarks")
                    time.sleep(1)
                    checkbox_elements = self.driver.find_elements(By.XPATH, "//span[@data-focus-id='selection-control']")  # получаем все элемнты содержащие данный xpath
                    checkbox_list = []

                    # формируем список чекбоксов
                    for d in checkbox_elements:
                        checkbox_list.append(d)

                    count = 0

                    # директория куда скачиваются файлы
                    # заменить на свой путь до папки
                    # заменить на свой путь до папки

                    original_file_path = "/Users/asilay/Desktop/bm/" # заменить на свой путь до папки

                    # перебираем список чекбоксов и скачиваем
                    for checkbox in checkbox_list[2:]:
                        # элемент не обязательно должен быть кликабельным (уникально идентифицируемым по координатам на экране и может находиться вне области видимости)
                        self.driver.execute_script("arguments[0].click();", checkbox)  # выбираем чекбокс
                        time.sleep(1)

                        # исключаем ошибку что кнопка "скачать" временно недоступен после выбора чекбокса
                        try:
                            wait = WebDriverWait(self.driver, 30)
                            download_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='download-object-button']")))
                        except StaleElementReferenceException:
                            continue

                        download_button.click()  # нажимаем кнопку скачать
                        count += 1
                        time.sleep(1)
                        self.driver.execute_script("arguments[0].click();", checkbox)  # снимаем выбор с чекбокса

                        # Переименование скачанного файла
                        file_list = os.listdir(original_file_path)
                        file_list.sort(key=lambda x: os.path.getctime(os.path.join(original_file_path, x)), reverse=True)  # сортируем список файлов по времени создания в обратном порядке
                        latest_file = file_list[0]  # выбираем последний добавленный файл
                        file_name, file_extension = os.path.splitext(latest_file)
                        current_datetime = datetime.datetime.now().strftime("%H.%M.%S")

                        # создаем новое имя добавляя к нему текущее время скачивания (исключаем замену файлов с одинаковыми именани)
                        new_file_name = f'{file_name}.{current_datetime}{file_extension}'
                        old = os.path.join(original_file_path, latest_file)
                        new = os.path.join(original_file_path, new_file_name)
                        os.rename(old, new)
                        print(f"Bookmark downloaded {count}")

                    self.driver.back()

                time.sleep(1)
                self.driver.back()

            self.driver.back()


        print(f'Основных папок: {len(selected_elements)}')
        print(f'Папок девайсов: {len(selected_elements_2)}')
