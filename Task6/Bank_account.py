
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number   #---->public access
        self._balance=balance     #----->protected modifiers

    def deposit(self,amount):
        self._balance+=amount
        print(f"amount deposited is {amount} total new balance is {self._balance}")

    def withdraw(self,amount):
        self._balance-=amount
        print(f"Amount withdraw is {amount} new balance is {self._balance}")

class SavingsAccount(BankAccount):
    def calculate_intrest(self,intrest):
        interest_amount=(self._balance/100)*intrest
        self._balance+=interest_amount
        print(f"Intrest added is {intrest} and new balance is {self._balance}")


class CurrentAccount(BankAccount):
    def minumum_balance(self,amount):
        if self._balance<500:
           print(f"you cannot withdraw amount {amount} as miminum balance is 500 your balnce is {self._balance}")
        else:
            self.withdraw(amount)


# New=Bank_Account('az113154',400)
# #******** Both are accessable one is public and other is protected*********
# print(New.account_number)
# print(New._balance)

New=CurrentAccount(12354,500)
print(New.account_number)
New.deposit(500)
New.withdraw(200)
New.minumum_balance(100)
New1=SavingsAccount('AZA744',500)
New1.calculate_intrest(5)
