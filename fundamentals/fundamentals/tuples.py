#tuples listed in paranthesis, however not 100% necessary

tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5 )
tuple_letters = "a", "b", "c", "d"

#tuples are immutable however tuples can be added or sliced
dog = ("Canis Familiaris", "dog", "carnivore", 12)
print(dog[2])
#result is: carnivore
dog[0] = "X"
#TypeError: 'tuple' object does not support item assignment
dog = dog + ("domestic",)
#result is...
#("Canis Familiaris", "Dog", "carnivore", 12, "domestic")
dog = dog[:3] + ("man's best friend",) + dog[4:]
#result is...
#("Canis Familiaris", "Dog", "carnivore", "man's best friend", "domestic")


#BUILT IN FUNCTIONS
x = (1,5,6,9,2)
print(len(x))
# output:
# 5

#max(sequence): returns largest value in sequence
#min(sequence): returns the sum of all values in sequence
#enumerate(sequence) used in a for loop context to return two-item-tuple for each item 
#   in sequence indicating the index followed by the value at that index
#map(function, sequence): applies the function to every item in the sequence you pass in
#   returns a list of the results
#min(sequence) returns the lowest value in sequence
#sorted(sequence): returns a sorted sequence

#using tuple as a return value
#functions can only return a single value, but tuple can be used to return a gorup of values
def get_circle_area(r):
    #Return (circumference, area) of a circle of radius r
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)

