# 1. TASK: print "Hello World"
print("Hello World!")
# 2. print "Hello Noelle!" with the name in a variable
name = "Natascha"
print("Hello",name, "!")	# with a comma
print("Hello" + name + "!")	# with a +
#3. print your favorite number in a variable
num = 13
print("Hello",num,"!") #with a comma
print("Hello"+str(num)+"!") # with a +, bonus: fix the error
#4. print "I love to eat {{fav_food_one}} and {{fave_food_two}}."
fave_food1 = "pho"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) #print with the format method 
print(f"I love to eat {fave_food1} and {fave_food2}.") #print with f-strings