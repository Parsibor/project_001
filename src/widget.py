from masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card: str) -> str:
    if account_card[:4].lower() == "счет":
        return "Счет " + get_mask_account(account_card[-20:])
        # return account_card[-16:]
    else:
        return account_card[0:-16] + " " + get_mask_card_number(account_card[-16:])
        return "Hello!"


if __name__ == "__main__":
    account_card = input("Введите карту или счет: ")
    print(mask_account_card(account_card))
    print(account_card[0:-16])

