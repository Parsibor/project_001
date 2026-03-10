from datetime import datetime
from typing import Any


def filter_by_state(data_list: list, state: str = "EXECUTED") -> list:
    """Функция, которая принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует
    указанному значению."""
    new_list: list[Any] = []

    for dict in data_list:
        if (
            "state" in dict
        ):  # Проверяем, есть ли в исходном списке "data_list" ключ "state" в каждом из словарей "dict"
            if dict["state"] == state:
                new_list.append(dict)
        else:
            # raise KeyError('В передаваемых данных отсутствует аргумент "state"')
            # Здесь могло бы вызываться исключение об отсутствии ключа в словаре, но я решил действовать более мягко
            # и применить пропуск итерации по добавлению записи в конечный список.

            continue  # Если ключа 'state' в словаре нет - пропускаем эту запись и не добавляем в конечный список.

    return new_list


def sort_by_date(data_list: list, sorting: bool = True) -> list:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция возвращает новый список, отсортированный по дате (date)."""

    """Аргумент sorting принимает значение по умолчанию True, чтобы сортировать список по убыванию"""

    list_sorted = sorted(
        data_list, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=sorting
    )
    return list_sorted


# --------------------------------------------------------------------------------------------
# if __name__ == "__main__":
#     test_list_filter_by_state = [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ]
#
#     test_list_filter_by_state2 = [
#         {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ]
#
#     test_list_filter_by_state3 = [
#         {"id": 41428829, "state": "ASD", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ]
#
# test_list_sort_by_date1 = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     {"id": 615064544, "state": "ASD", "date": "2017-10-14T08:21:33.419441"},
#     {"id": 615064591, "state": "ASD", "date": "2018-11-14T08:21:33.419441"}
# ]

# test_list_sort_by_date2 = [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}, # same date
#         {"id": 615064544, "state": "ASD", "date": "2017-10-14T08:21:33.419441"},
#         {"id": 615064591, "state": "ASD", "date": "2018-11-14T08:21:33.419441"},
#         {"id": 615064588, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"} # same date
#     ]

# test_list_sort_by_date3 = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"}, # same date
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"}, # same date
#     {"id": 594226727, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}, # same date
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}, # same date
#     {"id": 615064544, "state": "ASD", "date": "2017-10-14T08:21:33.419441"},
#     {"id": 615064591, "state": "ASD", "date": "2018-11-14T08:21:33.419441"},
#     {"id": 615064588, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"} # same date
# ]

#     print(filter_by_state(test_list_filter_by_state2, "EXECUTED"))
#     print(sort_by_date(test_list_sort_by_date1, True))
#     print(sort_by_date(test_list_sort_by_date2, True))
#     print(sort_by_date(test_list_sort_by_date3, True))
