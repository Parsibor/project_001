from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция, принимающая на вход один аргумент — строку, содержащую тип и номер карты или счета, и возвращает строку
    с замаскированным номером. Аргументом может быть строка типа Visa Platinum 7000792289606361, или
    Maestro 7000792289606361, или Счет 73654108430135874305."""

    if account_card[:4].lower() == "счет":
        mask_account = "Счет " + get_mask_account(account_card[-20:])
        return mask_account
    else:
        mask_card = account_card[0:-16] + " " + get_mask_card_number(account_card[-16:])
        return mask_card


def get_date(date: str) -> str:
    """Функция преобразует дату в виде 2024-03-11T02:26:18.671407 в формат ДД.ММ.ГГГГ"""
    new_date = date[8:10] + "." + date[5:7] + "." + date[:4]
    return new_date


if __name__ == "__main__":
    account_card = input("Введите карту или счет: ")
    print(mask_account_card(account_card))
    print(get_date("2024-03-11T02:26:18.671407"))
