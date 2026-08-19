class BankAccount:

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}")

    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount

            print(f"Withdrawn ₹{amount}")

        else:
            print("Insufficient Balance")

    def check_balance(self):

        print(
            f"Current Balance: ₹{self.__balance}"
        )


account = BankAccount(
    "Devasena",
    5000
)

account.check_balance()

account.deposit(2000)

account.withdraw(1500)

account.check_balance()
