# Создание списка из кубов нечетных чисел от 1 до 1000

list = range(1, 1000, 2)
# подзадача a.
# sum_n:int = 0
#
# for n in list:
#     cube = n ** 3
#     if cube % 7 == 0:
#         sum_n += cube
# print('Сумма чисел, которые делятся нацело на 7:', sum_n)


# подзадача b.
sum_n:int = 0
sum_n_17:int = 0

for n in list:
    cube = n ** 3
    cube_17 = (n + 17) ** 3
    if cube % 7 == 0:
        sum_n += cube
    if cube_17 % 7 == 0:
        sum_n_17 += cube_17
print('Сумма чисел, которые делятся нацело на 7:', sum_n)
print('Сумма чисел c элементом +17, которые делятся нацело на 7:', sum_n_17)