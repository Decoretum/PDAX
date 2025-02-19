from Infrastructure.AccountRepository import AccountRepository
from Infrastructure.CustomerRepository import CustomerRepository
from UseCase.GenerateIdentifiable import GenerateIdentifiable
from UseCase.CreateAccount import CreateAccount
from UseCase.MakeAccountStatements import MakeAccountStatements
from UseCase.MakeTransaction import MakeTransaction


#Repositories
AccRepo = AccountRepository()
CusRepo = CustomerRepository()

generator = MakeAccountStatements()
transaction = MakeTransaction(AccRepo)


AccountCreator = CreateAccount(CusRepo)

a1 = AccountCreator.create_account(1, "Gael", "gaelestrera@gmail.com", "09267174012")
a2 = AccountCreator.create_account(5, "Luka", "lukadoncic@gmail.com", "09892018824")
a3 = AccountCreator.create_account(5, "Luka", "lukadoncic@gmail.com", "09892018824")
a4 = AccountCreator.create_account(9, "Lebron", "lebronjames@gmail.com", "09524218592")

a1ID = a1.account_id
a2ID = a2.account_id
a3ID = a3.account_id

AccRepo.save_account(a1)
AccRepo.save_account(a2)
AccRepo.save_account(a3)

print('\n')

# Gathering accounts through customer_id
print(AccRepo.find_accounts_by_customer_id(5))

# Finding an account through account ID
print(AccRepo.find_account_by_id(a1ID))
print(AccRepo.find_account_by_id(a2ID))
print(AccRepo.find_account_by_id(a3ID))

print('\n\n\n')

# Finding Customers through customer_id
print(CusRepo.find_customer_by_customer_id(5).name)
print(CusRepo.find_customer_by_customer_id(1).name)

print("\n\n")
print("Present Customers")
for i in CusRepo.collection:
    print(i.name)

print('\n\n\n')

# Generating Account Statement
transaction.make_transaction(a1ID, 213, 'deposit')
transaction.make_transaction(a1ID, 2, 'withdraw')

transaction.make_transaction(a2ID, 4124, 'deposit')
transaction.make_transaction(a2ID, 2, 'deposit')
transaction.make_transaction(a2ID, 900, 'withdraw')


# This has been made possible since Account "a1" stored at the repository directly
# references object "a1"
s1 = generator.generate_account_statement(a1ID, AccRepo, CusRepo)
print(s1)
print('\n\n')
s2 = generator.generate_account_statement(a2ID, AccRepo, CusRepo)
print(s2)

print('\n\n')
transaction.make_transaction(a1ID, 5, 'deposit')

s3 = generator.generate_account_statement(a1ID, AccRepo, CusRepo)
print(s3)