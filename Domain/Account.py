class Account:
    def __init__(self, accId, cusId, accNum, bal):
        self.account_id = accId,
        self.customer_id = cusId,
        self.account_number = accNum,
        self.balance = bal

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance
    
    
