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

# ----------
# Understanding nested lists

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1][1])

# ----------
# Treasure map
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? (The size is 3x3): ")
column = int(position[0])
row = int(position[1])
selected_row = map[row - 1]
selected_row[column - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")

# ----------
# Rock, paper and scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# human choice
int_choice = input("\n\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n")
choice = int(int_choice)

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

# computer choice
comp_choice = random.randint(0,2)
if comp_choice == 0:
    print(rock)
elif comp_choice == 1:
    print(paper)
elif comp_choice == 2:
    print(scissors)

# comparison

if choice == comp_choice:
    print("It's a draw !!")
elif choice == 0 and comp_choice == 1:
    print("Computer won !!")
elif choice == 0 and comp_choice == 2:
    print("You won !!")
elif choice == 1 and comp_choice == 0:
    print("You won !!")
elif choice == 1 and comp_choice == 2:
    print("Computer won !!")
elif choice == 2 and comp_choice == 0:
    print("Computer won !!")
elif choice == 2 and comp_choice == 1:
    print("You won !!")
    