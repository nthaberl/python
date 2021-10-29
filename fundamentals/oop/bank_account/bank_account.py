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
        if self.balance <= 0:
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
            int_return = self.balance * self.int_rate
            self.balance += int_return
        return self
    
    @classmethod
    def accounts(cls):
        for x in BankAccount.all_accounts:
            print(f" Account Balances: ${x.balance}")


account1 = BankAccount(.01, 0)
account2 = BankAccount(.01, 0)

account1.deposit(50).deposit(50).deposit(50).withdraw(100).yield_interest().display_account_info()
account2.withdraw(50).display_account_info()

BankAccount.accounts()