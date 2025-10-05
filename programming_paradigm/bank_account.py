class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
        print("New account created with balance:", self.account_balance)
        
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited {amount}. New balance:", self.account_balance)
        else:
            print("Deposit amount must be a positive value")
                
    def withdraw(self, amount):
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                print(f"Withdrew {amount}. New balance:",self.account_balance)
                return True
            else:
                print("Insufficient funds")
                return False
        else:
            print("Withdrawal amount must be positive")
            return False
            
    def display_balance(self):
        print("Current balance:", self.account_balance)

