# Write a Python program to create a class representing a bank.
# Include methods for managing customer accounts and transactions.


class Account:
    def __init__(self, number, name, balance):
        self.number = number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account: {self.number}, Name: {self.name}, Balance: {self.balance}"

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value

    def transfer(self, account, value):
        self.withdraw(value)
        account.deposit(value)


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self):
        string = "{"
        for account in self.accounts:
            if string != "{":
                string += "; "
            string += str(account)
        string += "}"
        return string

    def get_account(self, number):
        for account in self.accounts:
            if account.number == number:
                return account
        return None


def main():
    try:
        bank = Bank()
        conta1 = Account(1, "Joao", 100)
        conta2 = Account(2, "Maria", 200)
        bank.add_account(conta1)
        bank.add_account(conta2)
        print(bank)
        conta1.deposit(100)
        print(conta1)
        conta1.withdraw(50)
        print(conta1)
        conta1.transfer(conta2, 50)
        print(conta1)
        print(conta2)
    except Exception as e:
        print("Erro: ", e)


if __name__ == "__main__":
    main()
