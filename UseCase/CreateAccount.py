from Domain.Account import Account
from Domain.Customer import Customer
from UseCase.GenerateIdentifiable import GenerateIdentifiable

class CreateAccount:
    def __init__ (self, customerRepository):
        self.customerRepository = customerRepository

    def create_account(self, customer_id, name, email, phone_number):
        IdentifiableGenerator = GenerateIdentifiable()
        accountId = IdentifiableGenerator.createId()
        accountNumber = IdentifiableGenerator.createNumber()

        newAccount = Account(accountId, customer_id, accountNumber, 0)
        newCustomer = Customer(customer_id, name, email, phone_number)

        existing = False
        for customer in self.customerRepository.collection:
            if customer.customer_id == customer_id:
                existing = True
                break

        if existing == True: 
            pass
        else:
            self.customerRepository.save(newCustomer)

        return newAccount