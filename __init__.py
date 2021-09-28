from flask import Flask
import csv

app = Flask(__name__)

categors = dict()    # словарь ключ-категория значение обьект(с полями ссылка и кол-во просмотров)

# функция чтения файла csv из той же директории
def read_file():
    # открытие файла
    with open("app\configfile.csv", encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель ","
        file_reader = csv.reader(r_file, delimiter=";")

        class Link():
            # класс Сылка на картинку

            count = 0        # кол-во просмотров
            link = ''        # сылка на картинку

            def __init__(self, link, count):
                self.count = count
                self.link = link

            def __str__(self):
                print(self.link, ' ', self.count)

        # Считывание данных из CSV файла
        for row in file_reader:
            try:
                lin = Link(row[0], int(row[1]))      # Создаем обект Ссылка с полями ссылки на картинку и кол-во просмотров
            except:
                print("Ошибка в составлении файла конфигурации")

            for colom in range(2, len(row)):     # считываем категории
                try:
                    categors[str(row[colom])].append(lin)   # добавляем категории в словарь в виде ключей
                except KeyError:                            # если не было создано пустого списка создаем его
                    print("Списка не было - создаем")
                    categors[str(row[colom])] = list()
                    categors[str(row[colom])].append(lin)

read_file()  # вызываем чтение файла при запуске сервера


from app import routes