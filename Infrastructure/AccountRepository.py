
class AccountRepository:
    def __init__(self):
        # Contains Account Objects
        self.collection = []

    def save_account(self, AccountObject):
        self.collection.append(AccountObject)

    def find_account_by_id(self, account_id):
        for acc in self.collection:
            if acc.account_id == account_id:
                return acc

    def find_accounts_by_customer_id(self, customer_id):
        accounts = []
        for acc in self.collection:
            if acc.customer_id == customer_id:
                accounts.append(acc)

        return accounts