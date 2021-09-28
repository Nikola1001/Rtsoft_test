import requests

# простой тест на общую проверку работоспособности

# запросы с ошибкой
links_bad = ["http://127.0.0.1:5000/?category[1]=caddddt1", 'http://127.0.0.1:5000/?catry[0]=ewr', 'http://127.0.0.1:5000/?category[0]=ccccc']

# запросы без ошибок (с получением картинки)
links_true = ["http://127.0.0.1:5000/?category[0]=ewr&category[1]=caddddt1", 'http://127.0.0.1:5000/?category[0]=ewr&category[1]=cat1', 'http://127.0.0.1:5000/?category[0]=cat3&category[1]=cat2', 'http://127.0.0.1:5000/?category[0]=cat3']

err = 0
for lin in links_bad:
    try:
        response = requests.get(lin)
    except:
        print("не удается получить ответ от сервера")
        break
    if not ("Картинки по выбранной(ыми) категорией(ями) нет") in response.text:
        print("Ошибка при запросе ", lin)
        err += 1
print("Тесты ошибочных запросов пройдены, ошибок ", err)

for lin in links_true:
    try:
        response = requests.get(lin)
    except:
        print("не удается получить ответ от сервера")
        break
    if not ("Найденная картинка") in response.text:
        print("Ошибка при запросе ", lin)
        err += 1
print("Тесты верных запросов пройдены, ошибок ", err)
