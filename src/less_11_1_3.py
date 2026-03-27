###########################
# Конвейерная разработка
###########################

from itertools import chain

# Удвоить каждый элемент списка
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x: x * 2, numbers)
print(list(doubled_numbers))

# Оставить только четные числа
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

# Объединить два списка в один
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list(chain(list1, list2))
print(list(combined_list))


# Функция-предикат для проверки четности числа
def is_even(x):
    return x % 2 == 0

# Функция для увеличения числа на 2
def add_two(x):
    return x + 2

# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Применение filter() для отбора четных чисел
even_numbers_2 = list(filter(is_even, numbers))

# Применение map() для увеличения каждого числа на 2
result = list(map(add_two, even_numbers_2))

print(result)
# Вывод: [4, 6, 8, 10, 12]