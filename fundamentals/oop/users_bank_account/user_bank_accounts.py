
class BankAccount:
# don't forget to add some default values for these parameters!
    all_accounts = []
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
    # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
    # your code here
        if self.balance - amount <= 0:
            print("Insufficient funds!! Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
    # your code here
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            # your code here
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def print_accounts(cls):
        for x in BankAccount.all_accounts:
            x.display_account_info()


class User:
    def __init__(self, name):
        self.name = name
        # self.account_balance = account_balance
        self.account = BankAccount(int_rate = .01, balance = 0)

    # def make_deposit(self):
    #     self.account.deposit(amount)
    #     print(self.account.balance)
    #     return self

    # def make_withdrawal(self, amount):
    #     self.account_balance -= amount
    #     return self

    def display_user_balance(self):
        print(f"Name: {self.name}, Account Balance: {self.account.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        other_user.display_user_balance()
        print(f"From: {self.name} To: {other_user.name} Amount Transferred: {amount}. {self.name} Balance: {self.account_balance}.")
        return self



user1 = User("Michael")
user1.account.deposit(100)
user1.account.display_account_info()
user2 = User("Guido")
user1.display_user_balance()
