class Account:
    def __init__(self, accId, cusId, accNum, bal):
        self.account_id = accId
        self.customer_id = cusId
        self.account_number = accNum
        self.balance = bal
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited PHP {amount}")
    
    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f"Withdrew PHP {amount}")

    def get_balance(self):
        return self.balance
    
    
