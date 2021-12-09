#OOP 4 Pillars

# 1. Encapsulation

class Human:
    def __init__(self):
        self.str = 10
        self.dex = 10
        self.int = 10
        self.hp = 100

    def attack(self, target):
        target.hp -= self.str

    def rest(self):
        self.hp += 10

# 2. Inheritance
# 3. Polymorphism
class Scholar(Human): #name of class we're inheriting from
    def __init__(self):
        super().__init__()
        self.int = 100
        self.str = 5
        self.dex = 5
        self.hp = 5

    def fireball(self, target):
        target.hp -= self.int

michael = Scholar()
# print("Str", michael.str)
# print("Dex", michael.dex)
# print("Int", michael.int)
# michael.rest()
# print("HP", michael.hp)

# print("=" * 40)

class Druid(Human): 
    def __init__(self):
        super().__init__()
        self.int = 60
        self.hp = 125

    def rest(self):
        self.hp += 30

nat = Druid()

# print("Str", nat.str)
# print("Dex", nat.dex)
# print("Int", nat.int)
# print("HP", nat.hp)
# nat.rest()
# print("HP", nat.hp)

print("=" * 40)

michael.fireball(nat)
print("Nat's HP", nat.hp)
nat.attack(michael)
print("Michael's HP", michael.hp)

#4 Abstraction
class Player:
    def __init__(self):
        self.name = "Kumari" #<-- does not have any of their own stats
        self.characterClass = Scholar()

    def attack(self,target):
        self.characterClass.fireball(target)

answer = input("What is the answer to the ultimate question of life, the universe, and everything??")
print(answer)