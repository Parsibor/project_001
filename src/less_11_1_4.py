###########################
# Генераторы списков
###########################

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []

# Здесь я показал, что спереди может стоять какое-то выражение, которое в целом может и не передавать переменной
# new_list_2 какие-то значения, а будет записывать фильтруемые значения в другой список - new_list:
new_list_2 = [new_list.append(x) for x in numbers if x % 2 == 0]

# А здесь как раз эталонное выражение, которое формирует в переменную new_list_3 список из элементов Х,
# возвращаемые после фильтрации с помощью IF
new_list_3 = [x for x in numbers if x % 2 == 0]

square = [x*x for x in range(20)]
result = [x for num in range(20) for x in [num, num] if x % 2 == 0]
ascii_codes = [ord(c) for c in "Hello!!!" if c.isalpha() and c.islower()]

# Возвращает индексы списка тех пар, элементы которых равны друг другу
matching_indices = [i for i, (x, y) in enumerate([(1, 2), (5, 5), (3, 1), (5, 0), (9, 16), (3, 3), (0, 0)]) if x == y]

# Задача: получить список чисел, которые делятся на 3 или на 5, в диапазоне от 1 до 100
list_3_5 = [x for x in range(1,101) if x % 3 == 0 or x % 5 == 0]

print(f"new_list = {new_list}")
print(f"new_list_2 = {new_list_2}")
print(f"new_list_3 = {new_list_3}")
print(f"square = {square}")
print(f"result = {result}")
print(f"ascii_codes = {ascii_codes}")
print(f"matching_indices = {matching_indices}")
print(f"list_3_5 = {list_3_5}")

