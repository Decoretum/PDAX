from Domain.Account import Account
from Domain.Customer import Customer
from UseCase.GenerateIdentifiable import GenerateIdentifiable

class CreateAccount:
    def create_account(self, customer_id, name, email, phone_number):
        IdentifiableGenerator = GenerateIdentifiable()
        accountId = IdentifiableGenerator.createId()
        accountNumber = IdentifiableGenerator.createNumber()

        newAccount = Account(accountId, customer_id, accountNumber, 0)
        # newCustomer = Customer(customer_id, name, email, phone_number)

        return newAccount