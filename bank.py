"""
TASK: Create a BankAccount class.

Requirements:
1. Each account should have an owner name and a starting balance.
2. Provide a method to deposit money.
3. Provide a method to withdraw money (only if sufficient balance).
4. Provide a method to check current balance.

Example Usage:
    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc.get_balance())  # 1300
"""

class BankAccount:
    def __init__(self):
        self.register = {}

    def account_details(self, owner_name, balance):
        self.register[owner_name] = {"owner_name": owner_name, "balance": balance}

    def deposit(self, name, amount):
        if name in self.register:
            if amount < 0:
                return "Invalid Amount!"
            else:
                self.register[name]["balance"] += amount
                return f"Amount: {amount} Deposited to {name} Sccessfully!"
        else:
            return f"{name} Not Found!"

    def withdraw(self, name, amount):
        if name in self.register:
            if amount > self.register[name]["balance"]:
                return f"Insuficient Funds!"

            else:
                self.register[name]["balance"] -= amount
                return f"Amount: {amount} withdrawn from Account Name: {name}" 

        else:
            return f"{name} Not Found!"

    def get_balance():
        pass

    def show_registration(self):
        return self.register


account = BankAccount()
account.account_details("John", 1000)
print(account.deposit("John", 500))
print(account.withdraw("John", 200))
print(account.show_registration())