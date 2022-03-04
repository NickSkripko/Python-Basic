# Домашнее задание 1_1

# a. до минуты <s> сек;
# duration = input('Введите продолжительность времени в секундах: ')
# print(duration, 'сек')

# b. до часа: <m> мин <s> сек;
# duration = int(input('Введите продолжительность времени в секундах: '))
# second = duration % 60
# minute = duration // 60
# if duration <= 59:
#     print(duration, 'сек')
# else:
#     print(minute, 'мин', second, 'сек')

# c. до суток: <h> час <m> мин <s> сек;
# duration = int(input('Введите продолжительность времени в секундах: '))
# second = duration % 60
# minute = duration // 60 % 60
# hour = duration // 3600
# if duration <= 59:
#     print(duration, 'сек')
# # изначально прописывал следующее условие для отображения минут: if duration >= 60 and duration <= 3599:
# if 60 <= duration <= 3599:
#     print(minute, 'мин', second, 'сек')
# else:
#     print(hour, 'час', minute, 'мин', second, 'сек')

# d.* в остальных случаях: <d> дн <h> час <m> мин <s> сек;
duration = int(input('Введите продолжительность времени в секундах: '))
second = duration % 60
minute = duration // 60 % 60
hour = duration // 3600 % 24
day = duration // 86400
if duration <= 59:
    print(duration, 'сек.')
else:
    if 60 <= duration <= 3599:
        print(minute, 'мин', second, 'сек')
    else:
        if 3600 <= duration <= 86399:
            print(hour, 'час', minute, 'мин', second, 'сек')
        else:
            print(day, 'дн', hour, 'час', minute, 'мин', second, 'сек')

# Вопрос: почему программа выводит неправильную комбинацию вывода данныхв двух вариантах:
# 1) когда ввожу продолжительность равную минутам и часам;
# 2) когда ввожу продолжительность равную секундам и минутам, выдает в две строки, правильный вариант и ниже неправильный;
# но код при этом работает.

# 1)
# duration = int(input('Введите продолжительность времени в секундах: '))
# second = duration % 60
# minute = duration // 60 % 60
# hour = duration // 3600 % 24
# day = duration // 86400
# if duration <= 59:
#     print(duration, 'сек.')
#     if 60 <= duration <= 3599:
#         print(minute, 'мин', second, 'сек')
#         if 3600 <= duration <= 86399:
#             print(hour, 'час', minute, 'мин', second, 'сек')
# else:
#     print(day, 'дн', hour, 'час', minute, 'мин', second, 'сек')
#
# # 2)
# duration = int(input('Введите продолжительность времени в секундах: '))
# second = duration % 60
# minute = duration // 60 % 60
# hour = duration // 3600 % 24
# day = duration // 86400
# if duration <= 59:
#     print(duration, 'сек')
# if 60 <= duration <= 3599:
#     print(minute, 'мин', second, 'сек')
# if 3600 <= duration <= 86399:
#     print(hour, 'час', minute, 'мин', second, 'сек')
# else:
#     print(day, 'дн', hour, 'час', minute, 'мин', second, 'сек')
