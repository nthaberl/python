#OOP

# The Hard Way

#I want to organize data that represents a dog

dog1 = {
    "name" : "Vicky",
    "age" : 4,
    "hair_color": "brindle"
}

dog2 = {
    "name" : "Leia",
    "age" : 0,
    "hair_color" : "red and white"
}

dog3 = {
    "name" : "Shiro",
    "age" : 9,
    "hair_color": "dirty white"
}

#The Better Way

    #class
        # custom data type
        # classes are a blueprint
        # use the class (blueprint) to create instances of the class(this is an object a.k.a. house)

# class Dog:
    # pass    # pass means literally do nothing/skip over

# dogObj1 = Dog() #creates an instance of the class Dog. Dog object instantiation (creating an object)


#attributes
    #variables in the class that every object instantiated from that class will have

#methods
    #are functions/actions, that an object can do
    #instance methods

#naming conventions
    #functions and variables snakecase
    #classes are Pascal case (UpperCamelCase)
    #ALWAYS SINGULAR

class Dog:
    num_of_dogs = 0 #this is our class attribute, this belongs to the class, not any object
    all_dogs = []
    #dunder / double underscore init function
    #init function is our constructor
    def __init__(self, name, age, hair_color): #always have self with instance method, represents the instance
        self.name = name
        self.age = age
        self.hair_color = hair_color #self.hair_color is an attribute
        Dog.num_of_dogs += 1 #everytime dog is called, it'll add to num_of_dogs
        Dog.all_dogs.append(self)
    #instance methods
    # refer to an individual object
    def fetch(self):
        print(f"BORF BORF, {self.name} is fetching the ball.")

    def eat(self):
        print(f"{self.name} is eating")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is getting older! It is now {self.age}")

    def drink(self):
        if(Dog.can_dog_drink_alcohol(self.age)):
            print(f"{self.name} is drinking dog beer")
        else:
            print(f"{self.name} is drinking dog kool-aid")

    #class methods
    #refers to the entire class, but decorator will only apply to next block of code
    @classmethod
    def get_num_of_dogs(cls):
        return dog.get_num_of_dogs

    @classmethod
    def print_all_dog_names(cls):
        for dog in Dog.all_dogs: #loops over list of dogs
            print(dog.name)

    #static methods
    # refers to nothing
    #static methods are stand alone functions that are included in a class
    @staticmethod
    def can_dog_drink_alcohol(age):
        return age >= 3


dog_obj1 = Dog("Vicky", 4, "brindle")
# print(dog_obj1)
# print(dog_obj1.name) #has to be called on separate lines
# print(dog_obj1.age)
# print(dog_obj1.hair_color)
# print(f"Dog 1.name: {dog_obj1.name}, Age: {dog_obj1.age}, Hair color: {dog_obj1.hair_color}")

dog_obj2 = Dog("Leia", 0, "red and white")
# print(dog_obj2)
# print(dog_obj2.name)
# print(dog_obj2.age)
# print(dog_obj2.hair_color)

dog_obj3 = Dog("Ralph", 3, "black")
dog_obj4 = Dog("Huck", 2, "red and white")
dog_obj5 = Dog("Oliver", 7, "white and brown")

# dog_obj1.fetch()
# dog_obj2.fetch()
# dog_obj1.eat ()
# dog_obj1.birthday()
# dog_obj1.birthday()
# dog_obj1.birthday()
# dog_obj1.birthday()
# print(f"Vicky's final age is {dog_obj1.age}")
print(Dog.num_of_dogs)
Dog.print_all_dog_names()
dog_obj1.drink()
dog_obj2.drink()
dog_obj3.drink()
dog_obj4.drink()
dog_obj5.drink()

class Person:
    def __init__(self, name):
        self.name = name

class Kennel:
    def __init__(self):
        self.name = "Humane Society of Pizza" #string
        self.owner = Person("Natascha") #person object
        self.dogs = [] #list of dog objects
    
    def add_dog (self, dog):
        self.dogs.append(dog)

kennel1 = Kennel()

print(kennel1.dogs)
kennel1.add_dog(dog_obj1)
kennel1.add_dog(dog_obj2)
kennel1.add_dog(dog_obj3)
kennel1.add_dog(dog_obj4)
kennel1.add_dog(dog_obj5)
print(kennel1.dogs)
print(kennel1.owner.name)