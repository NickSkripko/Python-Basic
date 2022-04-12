"""1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

"""Здесь проверял открытие файла для закрепления"""
# file_1 = open('nginx_logs.txt')
# text = file_1.read()
# print(text)

"""Сделал функцию парсинга"""
# def parse_nginx_logs(parse_file = 'nginx_logs.txt'):
#     with open(parse_file, 'r', encoding="utf-8") as f:
#         logs = []
#         for line in f:
#             logs.append(line.split(' - - ')[0])
#             logs.append(line.split('"')[1])
#             return logs


# print(parse_nginx_logs('nginx_logs.txt'))

"""2.* (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, 
размер которых превышает объем ОЗУ компьютера.
"""

# def spam_find(parse_file = 'nginx_logs.txt'):
#     parsed = parse_nginx_logs(parse_file)
#     spam = {}
#     for log in parsed:
#         spam[log[0]] = spam.get(log[0], 0) + 1
#     return max(spam.items(), key=lambda x: x[1])
### Тут произошел взрыв мозга... Видимо сильно усложнил задачу.

"""3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. 
Известно, что при хранении данных используется принцип: одна строка — один пользователь, 
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: 
ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные. 
Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None. 
Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, 
что объём данных в файлах во много раз меньше объема ОЗУ.

Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""

from itertools import zip_longest
import json

# users_hobby = {}
### С файлами формата .csv не получалось, так как я их создал не верно (использвола вариант через текстовый документ
### с сохранением .csv, но PyCharm выдает ошибку при выполнении кода. Поэтому заменил на формат .txt
# with open('users.txt', encoding='utf-8') as users:
#     with open('hobby.txt', encoding='utf-8') as hobby:
#         num_lines_users = sum(1 for line in users)
#         num_lines_hobby = sum(1 for line in hobby)
#
#         if num_lines_users < num_lines_hobby:
#             exit(1)
#
#         users.seek(0)
#         hobby.seek(0)
#         for line_user, line_user_hobby in zip_longest(users, hobby):
#             users_hobby[line_user.strip()] = line_user_hobby if line_user_hobby is None \
#                 else line_user_hobby.strip()
#
# with open('task3_DZ_6.json', 'w', encoding='utf-8') as f:
#     json.dump(users_hobby, f, ensure_ascii=False)
# print(users_hobby)

"""6. Реализовать простую систему хранения данных о суммах продаж булочной. 
Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных. 
При записи передавать из командной строки значение суммы продаж. 
Для чтения данных реализовать в командной строке следующую логику:
просто запуск скрипта — выводить все записи;
запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, 
по номер, равный второму числу, включительно.
Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:

python add_sale.py 5978,5
python add_sale.py 8914,3
python add_sale.py 7879,1
python add_sale.py 1573,7
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
7879,1
"""

# add_sale
import sys

sale = sys.argv[1]

with open('bakery.txt', 'a', encoding='utf-8') as f:
    f.write(sale)


# show_sales
import sys

sales = sys.argv[1:]
with open('bakery.txt', 'a', encoding='utf-8') as f:
    if len(sales) > 1:
        start_idx = int(sales[0])
        end_idx = int(sales[1])
    elif len(sales) == 0:
        start_idx = 0
        end_idx = sum(1 for line in f)
        f.seek(0)
    else:
        start_idx = int(sales[0])
        end_idx = sum(1 for line in f)
        f.seek(0)
    for idx, line in enumerate(f):
        if start_idx <= idx +1 <= end_idx:
            print(line.strip())