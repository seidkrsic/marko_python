

class Bank_account:
    total_accounts = 0

    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    
    def deposit(self, ammount):
        if Bank_account.is_valid_ammount(ammount) == True:  # True == True .... > True 
            self.balance += ammount
            print("success")
        else:
            print("not valid entry")
    
    @classmethod
    def account_count(cls):
        return cls.total_accounts
    
    @staticmethod
    def is_valid_ammount(ammount):
        if ammount>0:
            return True
        else:
            return False
    
Marko = Bank_account("Marko") 

Marko.deposit(500) 

print(Marko.balance) 

