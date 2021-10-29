# #1 
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# prediction: will print out 5
# actual: prints 5

# #2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# prediction: number_of_days_in_a_week_silicon_or_triangle_sides is not defined so will return an error
# actual: 'number_of_days_in_a_week_silicon_or_triangle_sides' is not definded

# #3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# prediction: will print 5 and then 10
# actual: only returns 5

# #4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# prediction: will print 10
# actual: only prints 5

# #5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# prediction: will print 5 and then 5
# actual: prints 5 and then none


# #6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# prediction: will print 8
# actual: TypeError: unsupported operand type(s) for +: "NoneType" and "NoneType"

# #7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# prediction: will print "2""5"
# actual: prints 25


# #8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#prediction: will print 100, then 10
#actual: prints 100, then 10


# #9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# prediction: will print 7, then 14, then 21
# actual: prints 7, then 14, then 21

# #10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# prediction: will print 8
# actual: prints 8

# #11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# prediction: will print 500, then 300, then 500, then 300, then 500
# actual: prints 500, then 500, then 300, then 500


# #12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# prediction: will print 500, 300, 500, 300, 500 
# actual: prints 500, 500, 300, 500


# #13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# prediction: will print 500, 500, 300, 300
# actual: prints 500, 500, 300, 300


# #14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# prediction: will print 1, 3 and then 2
# actual: prints 1, 3, then 2

# #15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# prediction: will print 1, 3, 5, 3, 5, 10
# actual: prints 1, 3, 5, 10