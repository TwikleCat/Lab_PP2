class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print({self.balance})
       
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance-=amount
            print(f"Withdraw:{amount}. Remaining balance: {self.balance}")


account = Account("Alice", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(150)