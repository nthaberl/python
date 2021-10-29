#basic
for x in range(0, 151):
    print(x)

#multiples of 5
for x in range (5, 1000, 5):
    print(x)

#counting, the Dojo Way: Print integers 1 to 100. 
#If divisible by 5, print "Coding" instead. 
#If divisible by 10, print "Coding Dojo".
for x in range(0, 101):
    if (x % 10 == 0):
        print("Coding Dojo")
        continue
    elif (x % 5 == 0):
        print("Coding")
        continue
    print(x)

#woah, that sucker's huge
#Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for x in range(0, 500001):
    if(x % 2 == 1):
        sum += x
print(sum)

#countdown by fours
#print positive numbers starting at 2018, countdown by fours
for x in range(2018, 0, -4):
    print(x)

#flexible counter
lowNum = 2
highNum = 9
mult = 3

for x in range(lowNum, highNum+1):
    if(x % mult == 0):
        print(x)