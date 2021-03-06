"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно.
Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
"""

# class Matrix:
#     def __init__(self, input_number):
#         self.input = input_number
#
#     def __str__(self):
#         return '\n'.join([' '.join(map(str, line)) for line in self.input])
#
#     def __add__(self, other):
#         result = ''
#         if len(self.input) == len(other.input):
#             for line_1, line_2 in zip(self.input, other.input):
#                 if len(line_1) != len(line_2):
#                     return 'Ошибка в размере матрицы'
#
#                 sum_line = [x + y for x, y in zip(line_1, line_2)]
#                 result += ' '.join(map(str, sum_line)) + '\n'
#         else:
#             return 'Ошибка в размере матрицы'
#         return result
#
# matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
# matrix_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
# matrix_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
# # print(matrix_3)
# print(matrix_1 + matrix_2)
# print(matrix_1 + matrix_3)
# print(matrix_2 + matrix_3)
#
# matrix_4 = Matrix([[8, 5, 1], [9, 4, 7], [2, -7, 0]])
# print(matrix_2 + matrix_4)

"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
 
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. 
К типам одежды в этом проекте относятся пальто и костюм. 

У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: 
для пальто (V/6.5 + 0.5), 
для костюма(2*H + 0.3). 
Проверить работу этих методов на реальных данных.

Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.

Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
"""

# from abc import ABC, abstractmethod
#
# class Clothes(ABC):
#     def __init__(self, size):
#         self.size = size
#
#     @abstractmethod
#     def material(self):
#         pass
#
# class Coat(Clothes):
#
#     @property
#     def material(self):
#         return self.size / 6.5 + 0.5
#
# class Suit(Clothes):
#
#     @property
#     def material(self):
#         return (2 * self.size) + 0.3
#
# coat = Coat(48)
# print(coat.material)
# suit = Suit(174)
# print(suit.material)
# print(coat.material + suit.material)

"""
3. Осуществить программу работы с органическими клетками, состоящими из ячеек. 
Необходимо создать класс «Клетка». 

В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). 

В классе должны быть реализованы методы перегрузки арифметических операторов: 
сложение (__add__()), 
вычитание (__sub__()), 
умножение (__mul__()), 
деление (__floordiv__, __truediv__()). 
Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и 
округление до целого числа деления клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.

Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.

Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества 
ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
Этот метод позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. 
В этом случае метод make_order() вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. 
Тогда метод make_order() вернёт строку: *****\n*****\n*****
"""


class Cell:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        return 'Сумма клеток равна: ' + str(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number > 0:
            return 'Разница клеток равна: ' + str(self.number - other.number)
        else:
            return 'Количество клеток не может быть меньше или равно нулю!'

    def __mul__(self, other):
        return 'Умножение клеток равно: ' + str(self.number * other.number)

    def __floordiv__(self, other):
        return 'Деление клеток равно: ' + str(round(self.number // other.number))

    def make_order(self, num):
        return '\n'.join(['*' * num for _ in range(self.number // num)]) + '\n' + '*' * (self.number % num)


cell_1 = Cell(33)
cell_2 = Cell(32)
print(cell_1)
print(cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(5))
