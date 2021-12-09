num1 = 42 #number variable declaration
num2 = 2.3 #decimal/float variable declaration
boolean = True #boolean variable declaration
string = 'Hello World' #string variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') #tuple initialize, immutable
print(type(fruit)) #type check
print(pizza_toppings[1]) #list access value
pizza_toppings.append('Mushrooms') #list add value
print(person['name']) #dictionary access value
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue' #dictionary add value
print(fruit[2]) #tuple access value


#conditionals below with just if and else statements
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

#conditionals with if, else if, and else statements
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# for loop start at 0 and goes up until 5
for x in range(5):
    print(x)
#for loop, start at 2 up until 5
for x in range(2,5):
    print(x)
#for loop, start at 2, go up until 10, increment by 3
for x in range(2,10,3):
    print(x)

x = 0 #while loop start point
while(x < 5): #while loop stop
    print(x)
    x += 1 #while loop increment

pizza_toppings.pop() #list delete value at end
pizza_toppings.pop(1) #list delete value at index

print(person)
person.pop('eye_color') #dictionary delete value
print(person)


for topping in pizza_toppings: #for loop through a list
    if topping == 'Pepperoni':     #conditional if
        continue #continues
    print('After 1st if statement')
    if topping == 'Olives': #conditional if
        break #stops the loop

#function declaration
def print_hello_ten_times():
    for num in range(10): #for loop starts at 0 up until 10
        print('Hello')

print_hello_ten_times() #function call

def print_hello_x_times(x): #function declaration with parameter x
    for num in range(x):  #for loop up until x
        print('Hello')

print_hello_x_times(4) #function call argument of 4

def print_hello_x_or_ten_times(x = 10): #function declaration with default parameter
    for num in range(x): #for loop up until x
        print('Hello') 

print_hello_x_or_ten_times() #call function with no argument since default goes up until 10
print_hello_x_or_ten_times(4) #call function with argument 


"""
Bonus section
"""

# print(num3) <--- NameError: name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry' <--- TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) <--- KeyError: 'favorite_team'
# print(pizza_toppings[7]) <--- - IndexError: list index out of range
#   print(boolean) <-- IndentationError: unexpected indent
# fruit.append('raspberry') <--- AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) <---AttributeError: 'tuple' object has no attribute 'pop'