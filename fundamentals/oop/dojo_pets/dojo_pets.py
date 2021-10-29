class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
    # implement the following methods:
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        return self
    def myPet(self):
        print(f"This is my {self.pet.type}, his name is {self.pet.name}")


class Pet(Ninja):
    # implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 50
        self.energy = 50
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f"Energy Level: {self.energy}")
        return self
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"Energy Level: {self.energy}, Health: {self.health}")
        return self
    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(f"Health: {self.health}")
        return self
    # noise() - prints out the pet's sound
    def noise (self):
        print("meow")
        return self
    def whatAmI (self):
        print(self.type)
        return self

Tofu = Pet("Tofu", "cat", "attack")
Taro = Pet("Taro", "cat", "jump")
Natascha = Ninja("Natascha", "H", "anchovies", "salmon", Tofu)
Emil = Ninja("Emil", "Ny", "yogurt", "chicken", Taro)

Natascha.walk()
# Natascha.bathe()
# print("Current Health:", Tofu.health)
# Emil.feed()
# print("Health:", Taro.health, "Energy", Taro.energy)
# Natascha.bathe().walk().feed()
# Tofu.whatAmI()
# Natascha.myPet()