"""1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield """

import sys

# def num_generator(max_num):
#     for num in range(1, max_num +1, 2):
#         yield num
#
# max_gen_33 = num_generator(33)
# for i in max_gen_33:
#     print(i)

"""2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), 
не используя ключевое слово yield."""

# num_gen = (num for num in range(1, 33 + 1, 2))
# print(type(num_gen))
#
# for i in num_gen:
#     print(i)

"""3. Есть два списка: tutors и klasses
 Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
 ('Иван', '9А')
 ('Анастасия', '7В')
 ...
 Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
 чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
 ('Станислав', None)"""

# tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

# tutor_klass = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
# print(next(tutor_klass))
# print(next(tutor_klass))
# print(next(tutor_klass))

# from itertools import zip_longest
#
# tutor_klass = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses) if tutors is not None)
# print(next(tutor_klass))
# print(next(tutor_klass))
# print(next(tutor_klass))
# print(next(tutor_klass))
# print(next(tutor_klass))
# print(next(tutor_klass))
# print(next(tutor_klass))
# print(next(tutor_klass))

"""4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
Подсказка: использовать возможности python, изученные на уроке."""

# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [num for i, num in enumerate(src) if num > src[i -1] and i != 0]
# print(result)

"""5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений. 
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации."""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [i for i in src if src.count(i) == 1]
print(result)