import pytest

from src.calculate_taxes import calculate_taxes

def test_calculate_taxes_value_under_zero():
    with pytest.raises(ValueError, match='Неверный налоговый процент'):
        calculate_taxes([100], -1)

def test_calculate_taxes_price_zero():
    with pytest.raises(ValueError, match='Неверная цена'):
        calculate_taxes([0], 0)

def test_calculate_taxes_prices_is_not_list():
    with pytest.raises(TypeError,match='Аргумент не является списком'):
        calculate_taxes(0,0)

