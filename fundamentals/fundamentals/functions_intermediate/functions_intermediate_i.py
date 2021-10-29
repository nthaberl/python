# UPDATE VALUES IN DICTIONARIES AND LISTS

#1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
#2. Change the last_name of the first student from 'Jordan' to 'Bryant'
#3. In the sports_directory, change 'Messi' to 'Andres'
#4. Change the value 20 in z to 30

# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# #1
# x[1][0] = 15
# print(x)

# #2 
# students[0]['last_name'] = "Bryant"
# print(students)

# #3
# sports_directory['soccer'][0] = "Andres"
# print(sports_directory)

# #4
# z[0]["y"] = 30
# print(z)

#ITERATE THROUGH A LIST OF DICTIONARIES
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# def iterateDictionary(list):
#     for x in range (len(list)):
#         for key in list[x]:
#             print (list[x][key])
# iterateDictionary(students)

#SOLUTION
def iterateDictionary(list):
    for x in range(0, len(list)):
        output=" "
    for key, val in list[x].items():
        output += f"{key} - {val},"
    print (output)

iterateDictionary(students)

#GET VALUES FROM A LIST OF DICTIONARIES
# create a function iterateDictionary2(key_name, some_list) that, 
# given a list of dictionaries and a key name
# the function prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB

# def iterateDictionary2(key_name, list):
#     for x in range (len(list)):
#             print (list[x][key_name])
# iterateDictionary2('first_name', students)

#And iterateDictionary2('last_name', students) should output:
# Jordan
# Rosales
# Guillen
# Tonel

#SOLUTION
# def iterate_dictionary2(key_name,list):
#     for i in range(0, len(list)):
        
#         for key,val in list[i].items():
#             if key == key_name:
#                 print(val)
# iterate_dictionary2('first_name',students)
# iterate_dictionary2('last_name',students)

# def iterateDictionary2(key_name, list):
#     for x in range (len(list)):
#             print (list[x][key_name])
# iterateDictionary2('last_name', students)


# print


# ITERATE THROUGH A DICTIONARY WITH LIST VALUES
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
# prints the name of each key along with the size of its list, and then prints the associated
# values within each key's list. For example:

# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

# def printInfo(some_dict):
#     for key in some_dict:
#         print(f"{len(some_dict[key])}{key.upper()}")
#         for x in range (len(some_dict[key])):
#             print(some_dict[key][x])
# printInfo(dojo)

#SOLUTION
# def print_info(dict):
#     for key,val in dict.items():
#         print("--------------")
#         print(f"{len(val)} {key.upper()}")
#         for i in range(0, len(val)):
#             print(val[i])

# print_info(dojo)