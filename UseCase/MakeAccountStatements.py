
class MakeAccountStatements:
    def __init__ (self):
        pass

    # returns a statement string containing transaction details for the queried account
    def generate_account_statement(self, account_id, accountRepository, customerRepository): 
        # Query Account
        acc = accountRepository.find_account_by_id(account_id)


        # The text itself
        print(f" ")
        print(f"Account Statement for Account ID {account_id}:", end='\n')
        for t in acc.transactions:
            print(t, end='\n')