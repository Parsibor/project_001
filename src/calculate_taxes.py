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


def calculate_tax(
        price: float,
        tax_rate: float,
        discount: float = 0,
        rounder: float = 2
) -> float:

    """Функция вычисляет стоимость товара с учетом налога и возвращает результат.
    - Возможность вычислять цену товара с учетом скидки. Скидка передается в виде аргумента,
    выраженного в процентах. Если скидки нет, значение равно 0. Функция должна вернуть
    стоимость товара с учетом налога и скидки (скидка берется от цены с учетом налога).
    - Добавлена Возможность округлять до заданного знака после запятой.
    - Добавлена обработка исключительной ситуации, возникающей при передаче аргументов типа,
    отличного от int или float."""

    for arg in [price, tax_rate, discount, rounder]:
        """Обработка исключительной ситуации, возникающей при передаче аргументов типа, 
        отличного от int или float"""
        if not isinstance(arg, (int | float)):
            raise TypeError("Ошибка типа данных")

    if price <= 0:
        raise ValueError('Неверная цена')

    if tax_rate < 0 or tax_rate >= 100:
        raise ValueError('Неверный налоговый процент')


    return round((price + (price * tax_rate / 100)) * (1 - discount / 100), rounder)



#--------------------------------------------------------------------------------------
if __name__ == '__main__':
    print(calculate_taxes([230,45,32], 5))
    print(calculate_tax(113, 13, 12))