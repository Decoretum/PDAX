
class MakeTransaction:
    def __init__(self, acc_repository):
        self.account_repository = acc_repository
    
    # trans type can either be "deposit" or "withdraw"
    # Updates Account balance
    def make_transaction(self, account_id, amount, transaction_type):
        # Query Account
        acc = self.account_repository.find_account_by_id(account_id)

        if transaction_type == "withdraw":
            if (acc.balance < amount):
                print("Cannnot withdraw from a bank account with a balance of PHP 0")
            else:
                acc.withdraw(amount)
        
        else:
            acc.deposit(amount)