from Infrastructure.AccountRepository import AccountRepository
from Infrastructure.CustomerRepository import CustomerRepository
from UseCase.GenerateIdentifiable import GenerateIdentifiable
from UseCase.CreateAccount import CreateAccount
from UseCase.MakeAccountStatements import MakeAccountStatements

#Account Statement Generator
generator = MakeAccountStatements()

AccRepo = AccountRepository()
CusRepo = CustomerRepository()

AccountCreator = CreateAccount(CusRepo)

a1 = AccountCreator.create_account(1, "Gael", "gaelestrera@gmail.com", "09267174012")
a2 = AccountCreator.create_account(5, "Samael", "Samael@gmail.com", "09278102865")
a3 = AccountCreator.create_account(5, "Luka", "lukadoncic@gmail.com", "09892018824")

a1ID = a1.account_id
a2ID = a2.account_id
a3ID = a3.account_id

AccRepo.save_account(a1)
AccRepo.save_account(a2)
AccRepo.save_account(a3)

# Gathering accounts through customer_id
print(AccRepo.find_accounts_by_customer_id(5))

# Finding an account through account ID
print(AccRepo.find_account_by_id(a1ID))
print(AccRepo.find_account_by_id(a2ID))
print(AccRepo.find_account_by_id(a3ID))

print('\n\n\n\n')

# Finding Customers through customer_id
print(CusRepo.find_customer_by_customer_id(5).name)
print(CusRepo.find_customer_by_customer_id(1).name)

print("\n\n")
print("Present Customers")
for i in CusRepo.collection:
    print(i.name)

print('\n\n\n\n')

# Generating Account Statement
a1.deposit(213)
a1.withdraw(2)

a2.deposit(4124)
a2.deposit(2)
a2.withdraw(900)

# This has been made possible since Account "a1" stored at the repository directly
# references object "a1"
generator.generate_account_statement(a1ID, AccRepo, CusRepo)
print('\n\n')
generator.generate_account_statement(a2ID, AccRepo, CusRepo)

print('\n\n')
a1.deposit(5)
generator.generate_account_statement(a1ID, AccRepo, CusRepo)