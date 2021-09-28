from app import app, categors
from flask import render_template, url_for
from flask import request


@app.route('/')
def search_category_link():
    # поиск картинки по запрошенной категории
    categs = []                # список категорий из запроса
    for i in range(0, 11):     # поиск категорий в запросе и добавление в список
        categs.append(request.args.get(f'category[{i}]'))

    path_image = ''                       # ссылка на нужную картинку
    error = ''                             # ошибка в запросе
    max_watch = 0       # наибольшее число показов
    # чтобы все картинки равномерно уменьшали показы (с наибольшим кол-вом выводятся первыми)
    for categ in categs:        # проход по категориям в запросе
        if categ:              # если не Нан
            try:
                for cat in categors[categ]:      # проход по обьетам Ссылка
                    if cat.count != 0 and max_watch < cat.count:   # если еще можно показывать и для этой картинки наибольшее чило показов
                        max_watch = cat.count
                        path_image = cat.link    # берем ссылку
                        cat.count -= 1             # уменьшаем кол-во показов
            except KeyError:                       # если была ошибка в запросе
                error = 'ошибка в названии категории (запросе)'

    # print(path_image)
    return render_template('index.html', path_image=path_image, error=error)

