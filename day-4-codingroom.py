# ----------
# Heads or Tails
import random
number = random.randint(0,1)
if number == 0:
    print("Tails")
else:
    print("Heads")

# ----------
# Exercise 2 - Banker Roulette
import random

name = input("Enter the names as comma separated values: ")
list_names = name.split(", ")
length = len(list_names)
int_length = int(length)
random_names = random.randint(1, int_length)
print(f"{list_names[random_names-1]} is going to buy the meal today !")