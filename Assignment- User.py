#
# 
#  make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.make_deposit(amount)
        return self

Sarah = User("Sarah","guido@email.com")
Samar = User("Samar","monty@email.com")
Norah = User("Norah","Norah@email.com")

Sarah.make_deposit(5000).make_deposit(100).make_deposit(20).make_withdrawal(5).display_user_balance()


Samar.make_deposit(50).make_deposit(100).make_withdrawal(2).make_withdrawal(3).display_user_balance()


Norah.make_deposit(200000).make_withdrawal(5000).make_withdrawal(200).make_withdrawal(300).display_user_balance()


Sarah.transfer_money(Norah,200).display_user_balance()

Norah.display_user_balance()
