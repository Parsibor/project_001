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

def test_calculate_tax_tax_rate_under_limit():
    with pytest.raises(ValueError, match='Неверный налоговый процент'):
        calculate_tax(12, -1)
        calculate_tax(12, 100)
        calculate_tax(12, 101)

def test_calculate_tax_discount():
    pass






# def test_calculate_tax_prices_and_tax_rate_is_not_float_1():
#     with pytest.raises(TypeError, match='Аргумент не является числом'):
#         calculate_tax(12, 'd')
#
# def test_calculate_tax_prices_and_tax_rate_is_not_float_2():
#     with pytest.raises(TypeError, match='Аргумент не является числом'):
#         calculate_tax('d', 12)
#
# def test_calculate_tax_prices_and_tax_rate_is_not_float_3():
#     with pytest.raises(TypeError, match='Аргумент не является числом'):
#         calculate_tax([12], 5)
#
# def test_calculate_tax_prices_and_tax_rate_is_not_float_4():
#     with pytest.raises(TypeError, match='Аргумент не является числом'):
#         calculate_tax((12,23,'ds'), 5)
#
# def test_calculate_tax_prices_and_tax_rate_is_not_float_5():
#     with pytest.raises(TypeError, match='Аргумент не является числом'):
#         calculate_tax(12, ['d', 14, True])
#
# def test_calculate_tax_prices_and_tax_rate_is_not_float_6():
#     with pytest.raises(TypeError, match='Аргумент не является числом'):
#         calculate_tax(12, (12,'d,True'))