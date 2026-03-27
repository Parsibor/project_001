"""
Задача 2
Чтение чисел из файла и их обработка
Дан текстовый файл nums.txt, содержащий список чисел, каждое число — на новой строке. Некоторые строки могут содержать
комментарии, начинающиеся с символа #. Необходимо считать числа из файла, проигнорировав комментарии и пустые строки.
Затем необходимо исключить из списка нечисловые элементы: nan, inf и -inf. После этого необходимо заменить
отрицательные числа на 0 и сложить все оставшиеся числа.
Результат необходимо вывести на экран в виде the sum is ЧИСЛО.
"""
# Ниже идут мои попытки пошагово избавиться от мусора, а ещё ниже решение, которое написал преподаватель!!!

# new_list = []
#
# with open('../data/num.txt', 'r', encoding='UTF-8') as f:
#     result = list(f)
#     for i in result:
#         new_i = i.replace('\n', '')
#         new_list.append(new_i)
#
# print('Сырые данные из файла')
# print(result)
# print("#" * 40)
# print('Данные очищенные от переноса строк')
# print(new_list)
# print("#" * 40)
#
# # for i in new_list:
#     # print(i)
#     # for x in i:
#
#     # if not int(i.isdigit()):
#     #     new_list.remove(i)
#
# # print("#" * 40)
# # print('Список без')
# # print(new_list)
# # print(f)

# --------------------------------------------------------------------------------
# Решение преподавателя
# Вот он закрутил, ебёна-мать!!!
import math

def clear_and_sum():
    with open('../data/num.txt', 'r', encoding='UTF-8') as file:
        rows = (row.split('#')[0].rstrip() for row in file) # Убираем всю фигню, где есть комменты с cимволом #
        nums = (float(n) for n in rows if n) # Преобразуем, что осталось в числа. Nan и inf - как бы тоже числа
        nums = (n for n in nums if math.isfinite(n)) # Убираем nan (ничего) и inf (бесконечность)
        nums = (max(0., n) for n in nums) # берём только положительные значения
        total_sum = sum(nums) # суммируем, что осталось

        return f'the sum is {total_sum}'

print (clear_and_sum())
