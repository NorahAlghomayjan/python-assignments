#  make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
from BankAccount import BankAccount

class User:		
    def __init__(self, name, email,accounts=1):
        self.name = name
        self.email = email
        self.accounts = []
        for i in range(accounts):
            self.accounts.append(BankAccount(int_rate=0.02, balance=0))
    
    def make_deposit(self, amount, accountNum = 1):	

        if len(self.accounts) < accountNum: return self

        self.accounts[accountNum-1].deposit(amount)
        return self
    
    def make_withdrawal(self, amount, accountNum = 1):

        if len(self.accounts) < accountNum: return self

        self.accounts[accountNum-1].withdraw(amount)
        return self

    def display_user_balance(self,accountNum=1):

        if len(self.accounts) < accountNum: return self

        print(f"User: {self.name}, ", end="")
        self.accounts[accountNum-1].display_account_info()
        return self

    def transfer_money(self, other_user, amount,accountNum=1,otherAccountNum=1):

        if len(other_user.accounts) < otherAccountNum: return self
        if len(self.accounts) < accountNum: return self

        self.accounts[accountNum-1].withdraw(amount)
        other_user.accounts[otherAccountNum-1].deposit(amount)
        return self

    def makeAnotherAccount(self):
        self.accounts.append(BankAccount(int_rate=0.02, balance=0))

Sarah = User("Sarah","guido@email.com")
Samar = User("Samar","monty@email.com")
Norah = User("Norah","Norah@email.com")
Fatimah = User("Fatimah","Fatimah@email.com",2)

Sarah.make_deposit(5000).make_deposit(100).make_deposit(20).make_withdrawal(5).display_user_balance()


Samar.make_deposit(50).make_deposit(100).make_withdrawal(2).make_withdrawal(3).display_user_balance()


Norah.make_deposit(200000).make_withdrawal(5000).make_withdrawal(200).make_withdrawal(300).display_user_balance()


Sarah.transfer_money(Norah,200).display_user_balance()

Norah.make_deposit(3000,2).transfer_money(Samar,2,2).display_user_balance(2)

Samar.display_user_balance(2)

Fatimah.make_deposit(600,2).display_user_balance(2)