import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, mask_expected",
    [
        ("1", "Введено неверное количество символов номера карты. Должно быть 16."),
        ("", "Введено неверное количество символов номера карты. Должно быть 16."),
        ("11112222333344445", "Введено неверное количество символов номера карты. Должно быть 16."),
        ("1111111111111111", "1111 11** **** 1111"),
    ],
)
def test_get_mask_card_number(card_number, mask_expected):
    assert get_mask_card_number(card_number) == mask_expected


@pytest.mark.parametrize("wrong_type", [(1), ([1]), ((1)), (True)])
def test_get_mask_card_number_type_error(wrong_type):
    with pytest.raises(TypeError):
        get_mask_card_number(wrong_type)


@pytest.mark.parametrize(
    "account_number, account_mask_expected",
    [("6363636363636363", "**6363"), ("123", "**123"), ("111122223333444455556666", "**6666")],
)
def test_get_mask_account(account_number, account_mask_expected):
    assert get_mask_account(account_number) == account_mask_expected
