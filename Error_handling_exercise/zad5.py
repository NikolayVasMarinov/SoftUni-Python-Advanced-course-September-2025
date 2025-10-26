class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass

pin_code, balance, age = input().split(", ")
balance: float = int(balance)
age: int = int(age)

while (command := input()) != "End":
    command_parts: list[str] = command.split("#")
    action, money = command_parts[:2]
    money: int = int(money)

    if action == "Send Money":
        pin: str = command_parts[2]

        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if pin != pin_code:
            raise PINCodeError("Invalid PIN code")

        if age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        balance -= money

        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    elif action == "Receive Money":
        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        balance += money / 2

        print(f"{money / 2:.2f} money went straight into the bank account")