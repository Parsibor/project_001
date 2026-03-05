def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    if type(prices) is not list:
        raise TypeError('Аргумент не является списком')

    taxed_prices = []

    for price in prices:
        if price <= 0:
            raise ValueError('Неверная цена')
        tax = price * tax_rate / 100
        taxed_prices.append(price + tax)

    return taxed_prices
#--------------------------------------------------------------------------------------


def calculate_tax(price: float, tax_rate: float, discount: float = 0, rounder: float = 2) -> float:

    # if type(price) or type(tax_rate) is not float:
    #     raise TypeError('Аргумент не является числом')

    if price < 0:
        raise ValueError('Неверная цена')

    if tax_rate < 0 or tax_rate >= 100:
        raise ValueError('Неверный налоговый процент')





    return round((price + (price * tax_rate / 100)) * (1 - discount / 100), rounder)



#--------------------------------------------------------------------------------------
if __name__ == '__main__':
    print(calculate_taxes([230,45,32], 5))
    print(calculate_tax(113, 13, 12))