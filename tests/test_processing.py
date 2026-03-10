import pytest

from src.processing import filter_by_state, sort_by_date

listing1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 615064544, "state": "ASD", "date": "2017-10-14T08:21:33.419441"},
    {"id": 615064591, "state": "ASD", "date": "2018-11-14T08:21:33.419441"},
]

# listing2 = [
#         {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
#     ]

listing3 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},  # same date
    {"id": 939719570, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},  # same date
    {"id": 594226727, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},  # same date
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},  # same date
    {"id": 615064544, "state": "ASD", "date": "2017-10-14T08:21:33.419441"},
    {"id": 615064591, "state": "ASD", "date": "2018-11-14T08:21:33.419441"},
    {"id": 615064588, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},  # same date
]


##############
# Проверка правильности выборки по ключу 'state'
##############
@pytest.mark.parametrize(
    "test_list, state, expected_list",
    [
        (
            listing1,
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        (
            listing1,
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            listing1,
            "ASD",
            [
                {"id": 615064544, "state": "ASD", "date": "2017-10-14T08:21:33.419441"},
                {"id": 615064591, "state": "ASD", "date": "2018-11-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state(test_list, state, expected_list):
    assert filter_by_state(test_list, state) == expected_list


##############
# Проверка правильности реагирования на отсутствие ключа 'state'
##############
# Закомментировал этот тест, т.к. применил в коде 'processing.py' другой способ, когда не вызывается исключение,
# а пропускается итерация по добавлению записи без ключа по 'continue'.

# def test_filter_by_state2():
#     assert filter_by_state(listing2)


# ---------------------------------------------------------------------------------------------------------------
##############
# Сортировка по возрастанию даты
##############
@pytest.mark.parametrize(
    "test_list, sorting, expected",
    [
        (
            listing1,
            False,
            [
                {"id": 615064544, "state": "ASD", "date": "2017-10-14T08:21:33.419441"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 615064591, "state": "ASD", "date": "2018-11-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        )
    ],
)
def test_sort_by_date_sort_up(test_list, sorting, expected):
    assert sort_by_date(test_list, sorting) == expected


##############
# Сортировка по убыванию даты
##############
@pytest.mark.parametrize(
    "test_list, sorting, expected",
    [
        (
            listing1,
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "ASD", "date": "2018-11-14T08:21:33.419441"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 615064544, "state": "ASD", "date": "2017-10-14T08:21:33.419441"},
            ],
        )
    ],
)
def test_sort_by_date_sort_down(test_list, sorting, expected):
    assert sort_by_date(test_list, sorting) == expected


##############
# Сортировка при одинаковых датах
##############
@pytest.mark.parametrize(
    "test_list, sorting, expected",
    [
        (
            listing3,
            True,
            [
                {"id": 615064591, "state": "ASD", "date": "2018-11-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 615064588, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 615064544, "state": "ASD", "date": "2017-10-14T08:21:33.419441"},
            ],
        )
    ],
)
def test_sort_by_date_sort_same_date(test_list, sorting, expected):
    assert sort_by_date(test_list, sorting) == expected


##############
# Тест на корректность формата даты
##############
# Пример данных для тестов
data = [
    {"date": "2024-01-01T12:00:00.000000", "state": "EXECUTED", "amount": 100},
    {"date": "2024-01-05T12:00:00.000000", "state": "CANCELLED", "amount": 200},
    {"date": "2024-01-03T12:00:00.000000", "state": "EXECUTED", "amount": 300},
    {"date": "2024-01-02T12:00:00.000000", "state": "EXECUTED", "amount": 400},
    {"date": "2024-01-05T12:00:00.000000", "state": "EXECUTED", "amount": 150},  # Одинаковая дата для тестирования
]


@pytest.fixture
def test_data():
    return data


@pytest.mark.parametrize(
    "date_string",
    [
        "invalid date",
        "2024/01/01T12:00:00.000000",  # Неверный формат
        "2024-01-01 12:00:00",  # Неверный формат (без T)
        "2024-01-01T12:60:00.000000",  # Неверная минута
    ],
)
def test_sort_by_date_invalid(test_data, date_string):
    # Тестирование сортировки с некорректным форматом даты
    with pytest.raises(ValueError):
        sort_by_date(test_data + [{"date": date_string}])
