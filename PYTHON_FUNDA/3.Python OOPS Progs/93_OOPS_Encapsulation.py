class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def get_balance(self):
        return self._balance

account = BankAccount("Amar", 100)
account.deposit(50)
print(account.get_balance())