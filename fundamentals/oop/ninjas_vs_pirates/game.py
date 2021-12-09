from classes.ninja import Ninja
from classes.pirate import Pirate
import random

michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

print("Would you like to be a Pirate or Ninja?")
player_select = input("Type P for pirate, N for Ninja")
if (player_select == "P"):
    print("Arrr you're a pirate")
elif (player_select == "N"):
    print("Nice, you're a ninja")

name = input ("What is your name?")

if (player_select == "P"):
    player = Pirate(name)
    opponent = Ninja("Shawn")
elif (player_select == "N"):
    player = Ninja(name)
    opponent = Pirate("Jim")

isTurn = True
while (opponent.health > 0 and player.health > 0):
    if (isTurn):
        player.attack(opponent)
        isTurn = False
    else:
        opponent.attack(player)
        isTurn = True
    print(f"Your health is {player.health}. Your opponent's health is {opponent.health}")

if (player.health > 0):
    print(f"You destroyed {opponent.name}")
else:
    print(f"You were wrecked by {opponent.name}, sucker")