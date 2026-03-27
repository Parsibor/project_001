import pytest

from src.less_11_1_10 import intersection_generator


def test_intersection_generator():
    # Создаем тестовые данные
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    expected_result = [3, 4, 5]

    # Запускаем генератор
    result = list(intersection_generator(list1, list2))

    # Проверяем, что результат соответствует ожидаемому
    assert result == expected_result

def test_empty_intersection():
    # Тест на случай, когда пересечений нет
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    expected_result = []

    # Запускаем генератор
    result = list(intersection_generator(list1, list2))

    # Проверяем, что результат — пустой список
    assert result == expected_result

def test_no_duplicates_in_output():
    # Тест на то, что в выводе нет дубликатов
    list1 = [1, 1, 1, 2, 2, 3]
    list2 = [1, 2, 2, 3, 3, 3]
    expected_result = [1, 2, 3]

    # Запускаем генератор
    result = list(intersection_generator(list1, list2))

    # Проверяем, что результат не содержит дубликатов
    assert result == expected_result
