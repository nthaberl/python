class User:
    pass

michael = User()
anna = User()

# declare a class and give it name User
class User:		
    def __init__(self): #self is a reference to the instance, not the class
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

# creating instances of user
User()
guido = User()
monty = User()
# Accessing the instance's attributes
print(guido.name)	# output: Michael
print(monty.name)	# output: Michael

guido.name = "Guido"
print(guido.name) # output: Guido
monty.name = "Monty"
print(monty.name) # output: Monty

#class attributes defined outside of any instances and shared among all instances
#more flexible because we can change them on an instance or the entire class

class User:
    # declaring a class attribute
    bank_name = "First National Dojo"		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

#changing on an instance
guido = User()
monty = User()
guido.bank_name = "Dojo Credit Union"
print(guido.bank_name) # output: Dojo Credit Union 
print(monty.bank_name) # output: First National Dojo

#changing on an entire class
User.bank_name = "Bank of Dojo"
print(guido.bank_name) # output: Bank of Dojo 
print(monty.bank_name) # output: Bank of Dojo

#passing in arguments
#do not need argument for self
#will assume everyone starts with $0
# class User:
#     # class attributes get defined in the class 
#     bank_name = "First National Dojo"
#     # now our method has 2 parameters!
#     def __init__(self , name, email_address):
    	# we assign them accordingly
            # self.name = name
            # self.email = email_address
    	# the account balance is set to $0
            # self.account_balance = 0
        class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# added this line
        #adding deposit method
        def make_deposit(self, amount): # takes an argument that is the amount of the deposit
            self.account_balance += amount	# the specific user's account increases by the amount of the value received
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50

#methods have access to class' attributes


#@class Methods
    #It's important to know that class methods 
    #have no access to the instance attribute or any attribute that starts with self.
class BankAccount:
    # class attribute
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum


#@staticmethods
#no access to instance or class attributes so no arguments need to be passed into them
class BankAccount:
    # ... __init__ goes here
    def with_draw(self,amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self    
    # static methods have no access to any attribute
    # only to what is passed into it
    @staticmethod
    def can_withdraw(balance,amount):
    	if (balance - amount) < 0:
	    return False
        else:
	    return True

