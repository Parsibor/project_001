import pytest

from src.calculate_taxes import calculate_taxes, calculate_tax

def test_calculate_taxes_value_under_zero():
    with pytest.raises(ValueError, match='Неверный налоговый процент'):
        calculate_taxes([100], -1)

def test_calculate_taxes_price_zero():
    with pytest.raises(ValueError, match='Неверная цена'):
        calculate_taxes([0], 0)

def test_calculate_taxes_prices_is_not_list():
    with pytest.raises(TypeError,match='Аргумент не является списком'):
        calculate_taxes(0,0)
#--------------------------------------------------------------------------------------

def test_calculate_tax_price_under_zero():
    with pytest.raises(ValueError, match='Неверная цена'):
        calculate_tax(-1, 1)

def test_calculate_tax_price_zero():
    with pytest.raises(ValueError, match='Неверная цена'):
        calculate_tax(0, 1)

def test_calculate_tax_tax_rate_under_limit():
    with pytest.raises(ValueError, match='Неверный налоговый процент'):
        calculate_tax(12, -1)
        calculate_tax(12, 100)
        calculate_tax(12, 101)



@pytest.mark.parametrize("price, tax_rate, discount, rounder", [('100', 5, 20, 2),
                                                                (200, '12', 4, 2),
                                                                (400, 3, '23', 3),
                                                                (213, 12, 43, '1')])

def test_calculate_tax_wrong_type(price, tax_rate, discount, rounder):
    with pytest.raises(TypeError):
        calculate_tax(price, tax_rate, discount, rounder)

