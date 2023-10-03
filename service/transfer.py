import os

class Transfer():

    def __init__(self, driver):
        super().__init__()
        self.driver = driver


    def change_format(self):

        folder = '/Users/asilay/Desktop/bm/'  # указать свой путь до папки
        file = os.listdir(folder)
        for file_name in (file):
            if file_name.endswith(('.kml', '.gpx')):
                continue
            else:
                new_file_name = f'{file_name}.kmz'
                old_path = os.path.join(folder, file_name)
                new_path = os.path.join(folder, new_file_name)
                os.rename(old_path, new_path)
        print("Формат изменен")