import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)

transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


@pytest.fixture
def transactions_():
    return transactions

#-----------------------------------------------------------------------------------------

@pytest.mark.parametrize("transact, currency_code, expected_count", [
    (transactions, "USD", 3),  # Три транзакции в USD
    (transactions, "RUB", 2),  # Одна транзакция в RUB
    (transactions, "EUR", 0),  # Нет транзакций в EUR
    ([], "USD", 0)  # Пустой список
])
def test_filter_by_currency(transact, currency_code, expected_count):
    # print(transact)
    result = list(filter_by_currency(transact, currency_code))
    assert len(result) == expected_count

#-----------------------------------------------------------------------------------------

@pytest.mark.parametrize("expected_descriptions", [
    [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]
])

def test_transaction_descriptions_with_values(transactions_, expected_descriptions):
    # Проверяем, что для всех транзакций из фикстуры получаем правильные описания
    # print(transactions_)
    result = list(transaction_descriptions(transactions_))
    assert result == expected_descriptions

def test_transaction_descriptions_with_zero_value(transactions_):
    result = list(transaction_descriptions(transactions_))
    # Проверка на пустой список
    assert list(transaction_descriptions([])) == []

#-----------------------------------------------------------------------------------------

@pytest.mark.parametrize("range_in, range_out, expected", [
    (
        1,
        5,
        [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005"
        ]
    ),
    (
        333,
        338,
        [
            "0000 0000 0000 0333",
            "0000 0000 0000 0334",
            "0000 0000 0000 0335",
            "0000 0000 0000 0336",
            "0000 0000 0000 0337",
            "0000 0000 0000 0338",
        ]
    ),
    (
        9999999999999998,
        9999999999999999,
        [
            "9999 9999 9999 9998",
            "9999 9999 9999 9999"
        ]
    ),
    (
        9999999999999998,
        99999999999999999,
        []
    ),
    (
        99999999999999988,
        9999999999999999,
        []
    ),
    (
        9999999999999999,
        9999999999999997,
        []
    ),
    (
        5,
        3,
        []
    ),
    (
        0,
        5,
        []
    ),
    (
        -10,
        5,
        []
    )
])

def test_card_number_generator(range_in, range_out, expected):
    assert list(card_number_generator(range_in, range_out)) == expected





