fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)
#can hold multiple data types, ideally keep it all the same

#accessing values
drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print(drawer[0])  #prints documents
#access the drawer with index of 1 and print value
print(drawer[1]) #prints envelopes
#access the drawer with index of 2 and print value
print(drawer[2]) #prints pens

#manipulating lists

#appends a new itom onto the END of a given list, you can pass in any data type
x = [1,2,3,4,5]
x.append(99)
print(x)
#the output would be [1,2,3,4,5,99]

#returns list constrained at certain indices
x = [99,4,2,5,-3]
print(x[:])
#the output would be [99,4,2,5,-3]
print(x[1:])
#the output would be [4,2,5,-3];
print(x[:4])
#the output would be [99,4,2,5]
print(x[2:4])
#the output would be [2,5];


#BUILT IN FUNCTIONS

#len(sequence): returns number of items in a sequence
my_list = [1, 'Zen', 'hi']
print(len(my_list))
# output
3

#enumerate(sequence) -- used in a for loop context to return two-item-tuple for each item
#   in the list inidicating the index followed by the value at that index
#map(function, sequence) apples the function to every item in the sequence you pass in. 
#   returns a list of the results
#min(sequence) returns the lowest value in a sequence
#sorted (sequence) retunrs a sorted sequence

#BUILT IN METHODS

#list.append(value)
my_list = [1,5,2,8,4]
my_list.append(7)
print(my_list)
# output:
# [1,5,2,8,4,7]


#list.extend(list2) adds all values from a second sequence to the end of the original
#list.pop(index) remove a value at a given position, default is final value in list
#list.index(value) returns the index position in a list for given parameter
