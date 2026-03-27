import random
from statistics import mean

# Задача 1
# Напишите генератор, который принимает на вход последовательность чисел и генерирует квадраты этих чисел.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [7,8,9,11,12,13,14,15,16,17,18,19,20]

squares = list((x * x for x in numbers))
print(squares)
print('#' * 20)
#--------------------------------------------------------------------------------------

# Задача 2
# Напишите генератор, который генерирует случайные числа в заданном диапазоне.

rand = random.randint(1, 100000)

print(rand)
print('#' * 20)
#--------------------------------------------------------------------------------------

# Попутно нашел, как вычислить среднее арифметическое через статистическую функцию )))
print(mean(numbers))
print('#' * 20)
#--------------------------------------------------------------------------------------

# Задача 3
# Напишите генератор, который генерирует последовательность чисел по заданной формуле.

def sequence_generator(start, formula):
    num = start
    while True:
        yield num
        num = formula(num)

# Определяем формулу как функцию, которая добавляет 1
formula = lambda x: x + 1

# Создаем генератор
gen = sequence_generator(0, formula)

# Получаем первые 5 чисел из генератора
for _ in range(5):
    print(next(gen))
print('#' * 20)
# --------------------------------------------------------------------------------------

# Задача 4
# Напишите генератор, который принимает на вход два списка и генерирует элементы, которые есть в обоих списках.
def intersection_generator(list1, list2):
    summ = set()
    for item in list1:
        if item in list2 and item not in summ:
            summ.add(item)
            yield item
# Я нихуя не понял, что ту происходит!!!!!!!!!!!!
# Точнее понял, но оно какого-то хуя возвращает как-будто бы не то, что я хочу.
# Быть может я делаю неправильный вызов??? И так, и сяк, и наперекосяк, ХЗ, короче!

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_list_2 = [7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# print(*intersection_generator(numbers_list, numbers_list_2))
# print(next(intersection_generator(numbers_list, numbers_list_2)))
# print(next(intersection_generator(numbers_list, numbers_list_2)))
# print(next(intersection_generator(numbers_list, numbers_list_2)))
# А вот тут я НИХУЯ не понял, почему вызов каждого NEXT не формирует следующее пересечение элементов двух
# списков???? Да пиздец!!!

g = intersection_generator(numbers_list, numbers_list_2)
print(next(g))
print(next(g))
print(next(g))
# Вот суки какие! Получилось, ебать вас в сраку!

print('#' * 20)
#--------------------------------------------------------------------------------------

# * Задача 6
# Это дополнительная задача. Выполняйте ее, когда решите все предыдущие задачи.
# Напишите генератор, который принимает на вход размерность квадратной матрицы и генерирует числа по спирали,
# начиная с центрального элемента.

# def spiral_generator(n):
#     matrix = [[0] * n for _ in range(n)]
#     x, y = n // 2, n // 2
#     dx, dy = 0, -1
#     num = 1
#
#     for _ in range(n * n):
#         if -n // 2 < x <= n // 2 and -n // 2 < y <= n // 2:
#             matrix[y][x] = num
#             yield num
#             num += 1
#
#         if x == y or (x < y and x + y < n - 1) or (x > y and x + y >= n):
#             dx, dy = -dy, dx
#
#         x, y = x + dx, y + dy

def spiral_generator(n):
    matrix = [[0] * n for _ in range(n)]
    x, y = n // 2, n // 2
    dx, dy = 0, -1
    num = 1

    for _ in range(n * n):
        if 0 <= x < n and 0 <= y < n:  # Проверяем, что координаты в пределах матрицы
            matrix[y][x] = num
            yield num
            num += 1

        # Поворот на 90 градусов
        if (x == y) or (x < y and x + y == n - 1) or (x > y and x + y == n):
            dx, dy = -dy, dx

        x, y = x + dx, y + dy
# spiral = spiral_generator(5)

# print(*spiral)
# print(*spiral_generator(101))
# print(next(spiral))
# print(next(spiral))
# print(next(spiral))
# print(next(spiral))

# Определяем размерность матрицы
n = 101

# Создаем генератор для матрицы размером n x n
spiral_gen = spiral_generator(n)

# Получаем первые несколько чисел из генератора
try:
    for _ in range(n * n):  # Ожидаем n*n чисел, так как это кол-во элементов в матрице
        print(next(spiral_gen))
except StopIteration:
    print("Генератор завершил работу")

# Ебанина какая-то, а не генератор и логика мне его не понятна.

#--------------------------------------------------------------------------------------

if __name__ == '__main__':
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers_list_2 = [7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    # assert list_same(numbers_list, numbers_list_2) == numbers_list
    # --------------------------------------------------------------------------------------








