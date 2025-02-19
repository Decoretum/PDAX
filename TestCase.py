from Infrastructure.AccountRepository import AccountRepository
from UseCase.GenerateIdentifiable import GenerateIdentifiable
from UseCase.CreateAccount import CreateAccount

AccRepo = AccountRepository()
AccountCreator = CreateAccount()

a1 = AccountCreator.create_account(1, "Gael", "gaelestrera@gmail.com", "09267174012")
a2 = AccountCreator.create_account(5, "Samael", "Samael@gmail.com", "09278102865")
a3 = AccountCreator.create_account(5, "Luka", "lukadoncic@gmail.com", "09892018824")

AccRepo.save_account(a1)
AccRepo.save_account(a2)
AccRepo.save_account(a3)

print(AccRepo.find_accounts_by_customer_id(5))
print((a2.customer_id))
