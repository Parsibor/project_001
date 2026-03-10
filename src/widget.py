from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция, принимающая на вход один аргумент — строку, содержащую тип и номер карты или счета, и возвращает строку
    с замаскированным номером. Аргументом может быть строка типа Visa Platinum 7000792289606361, или
    Maestro 7000792289606361, или Счет 73654108430135874305."""

    if isinstance(account_card, str):  # Проверяем, что аргумент точно строка, иначе вызывается ошибка типа
        if account_card[:4].lower() == "счет":
            mask_account = "Счет " + str(get_mask_account(account_card[-20:]))
            return mask_account
        else:
            mask_card = str(account_card[0:-16]) + str(get_mask_card_number(account_card[-16:]))
            return mask_card
    else:
        raise TypeError("Ошибка типа входных данных")


def get_date(date: str) -> str:
    """Функция преобразует дату в виде 2024-03-11T02:26:18.671407 в формат ДД.ММ.ГГГГ"""
    if isinstance(date, str):
        if len(date) >= 10:
            if date[4] == "-" and date[7] == "-":  # Если дата в формате 2024-03-11T02:26:18.671407
                new_date = date[8:10] + "." + date[5:7] + "." + date[:4]
                return new_date
            elif date[2] == "/" and date[5] == "/":  # Если дата в формате 11/03/2024
                new_date = date[:2] + "." + date[3:5] + "." + date[6:10]
                return new_date
            else:
                return "В поле ДАТА передано что-то не то!"
        else:
            return "Передан неверные формат или длина даты"
    else:
        raise TypeError("Ошибка типа входных данных")


# ----------------------------------------------------------------------------------------------
# if __name__ == "__main__":
#     account_card = input("Введите карту или счет: ")
#     print(mask_account_card(account_card))
#
#     print(get_date("2024-03-11T02:26:18.671407"))
#     print(get_date("2024-03-11T02:"))
#     print(get_date("2024-03-1"))
#     print(get_date("202"))
#     print (get_date("12/12/2023"))
#     print (get_date())


# print(get_date("2024-03-11T02:26:18.671407"))
# print(get_date("2024-03-11T02:26:18.671407"))
