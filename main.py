from abc import ABC, abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def account_type(self):
        pass
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def withdraw(self, amount):
        if amount <= 0 :
            print("Invalid amount")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
    def display_info(self):
        print(self.owner)
        print(self.get_balance ())
        
class SavingsAccount(BankAccount):
    def account_type(self):
        return "Savings"
    def calculate_interest(self):
        return self.get_balance() * 0.05
    
class CheckingAccount(BankAccount):
    def account_type(self):
            return "Checking"
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        else:
            total = amount + 10
            super().withdraw(total)
            


accounts = [
    SavingsAccount("Amal", 500),
    CheckingAccount("Amal", 500)
    
]
for account in accounts:
    account.withdraw(100)
    print(account.get_balance())

checking = CheckingAccount("Amal", 500)
checking.withdraw(100)       
print(checking.get_balance())
savings = SavingsAccount("Amal", 5000) 
print(savings.get_balance()) 
#account = BankAccount("Amal", 3000)
account.withdraw(5000)
account.display_info()
print(account.get_balance())
print(savings.calculate_interest())
print(savings.account_type())
print(checking.account_type())
print(account.account_type())



