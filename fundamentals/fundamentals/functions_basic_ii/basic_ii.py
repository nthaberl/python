# #1
list = []
def countdown(highNum):
    for x in range(highNum, -1, -1):
        list.append(x)
    print (list)
countdown(5)

# #2
def print_and_return(list):
    print(list[0])
    return(list[1])
print(print_and_return ([1,2]))

# #3 
def first_plus_length(list):
    sum = list[0]+len(list)
    return(sum)
print(first_plus_length([1,2,3,4,5]))

#4
def values_greater_than_second(list):
    new_list = []
    if len(list) < 2:
        return False
    for x in range (0, len(list)):
        if list[x] > list[1]:
            new_list.append(list[x])
    return(new_list)

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# #5
def length_and_value (length,value):
    new_list = []
    for x in range (0, length+1):
        new_list.append(value)
    print(new_list)

length_and_value(4,7)
length_and_value(6,2)
