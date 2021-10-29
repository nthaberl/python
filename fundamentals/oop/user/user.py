#make_withdrawal(self, amount) - 
    #have this method decrease the user's balance by the amount specified
#display_user_balance(self) - have this method print the user's name and account balance 
    #to the terminal eg. "User: Guido van Rossum, Balance: $150
#BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance 
    #by the amount and add that amount to other other_user's balance
class User:
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = account_balance
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"Name: {self.name}, Account Balance: {self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        other_user.display_user_balance()
        print(f"From: {self.name} To: {other_user.name} Amount Transferred: {amount}. {self.name} Balance: {self.account_balance}.")
        return self

michael = User("Michael", 500)
guido = User("Guido", 75)
monty = User("Monty", 6500)

michael.make_deposit(50).make_deposit(100).make_deposit(125).make_withdrawal(66).display_user_balance().transfer_money(monty, 40)
guido.make_deposit(5000).make_deposit(3500).make_withdrawal(1500).make_withdrawal(1337).display_user_balance()
monty.make_deposit(20).make_withdrawal(500).make_withdrawal(1040).make_withdrawal(5000).display_user_balance()