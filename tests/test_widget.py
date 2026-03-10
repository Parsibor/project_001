import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(arg, expected):
    assert mask_account_card(arg) == expected


@pytest.mark.parametrize("wrong_type", [(1), ([1]), ((1)), (True)])
def test_mask_account_card_type_error(wrong_type):
    with pytest.raises(TypeError):
        mask_account_card(wrong_type)


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11T02:26", "11.03.2024"),
        ("2024-03-1", "Передан неверные формат или длина даты"),
        ("", "Передан неверные формат или длина даты"),
        ("12/12/2023", "12.12.2023"),
        ("ssssssssssssssssssssss", "В поле ДАТА передано что-то не то!"),
    ],
)
def test_get_date1(date, expected):
    assert get_date(date) == expected


@pytest.mark.parametrize("wrong_type", [(1), ([1]), ((1)), (True)])
def test_get_date_type_error(wrong_type):
    with pytest.raises(TypeError):
        get_date(wrong_type)
