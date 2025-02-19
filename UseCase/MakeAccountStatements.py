
class MakeAccountStatements:
    def __init__ (self):
        pass

    # returns a statement string containing transaction details for the queried account
    def generate_account_statement(self, account_id, accountRepository, customerRepository): 
        # Query Account
        acc = accountRepository.find_account_by_id(account_id)

        # Query Customer
        cus = customerRepository.find_customer_by_customer_id(acc.customer_id)


        # The text itself
        statementString = ""
        statementString += (f"Account Statement for Account ID {account_id}:")
        statementString += '\n'
        statementString += (f"Account Number: {acc.account_number}")
        statementString += '\n'

        statementString += (f"Account Owner: {cus.name}")
        statementString += '\n'
        statementString += (f"Total Balance of Account: {acc.balance}")
        statementString += '\n'
        
        for t in acc.transactions:
            statementString += (t)
            statementString += '\n'

        return statementString