weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

#accessing values
print(weekend["Sun"])
print(capitals["svk"])

#removing values
value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
del capitals['dnk'] # will delete the key, and not return anything

#nested dictionaries
context = {
    'questions': [
        { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
        { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
        { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
        { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
    ]
}

#BUILT-IN FUNCTIONS AND METHODS
#cmp(dict1,dict2):  Compares two dictionaries. 
#   The comparison process starts with the length of each dictionary, followed by key names, followed by values. 
#   The function returns 0 if the two dicts are equal, -1 if dict1 > dict2, 1 if dict1 < dict2.
#len(): give the total length of dictionary
#str(): produces a string respresentation of a dictionary
#type(): returns the type of the passed variable. if passed variable is a dictionary, will return a dict type
#python includes the following methods either dict.method(yourDictionary) or yourDictionary.method() work
#.clear() removes all elements in dictionary
#.copy() returns a shallow copy of dictionary
#.fromkeys(sequence, [value]) create a new dictionary with keys from a sequence and values set to value
#.get(key, default=None) for key key, returns value or default if key is not in dictionary
#.has_key.(key) returns true if a given key is available in the dictionary, otherwise it returns false.
#.items() returns a list of dictionary's (key, value) tuple pairs
#.keys() return a list of dictionary keys
#.setdefault(key, default=None) similar to get(), but will set dict[key]=defualt if key is not already in dictionary
#.update(dict2) = adds dictionary 2's key-value pairs to an existing dictionary
#.values() returns list of dictionary values
