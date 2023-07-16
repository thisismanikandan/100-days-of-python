# coding rooms' Exercise 1 - Printing

# printing everything in single line
print("\nDay 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")

# printing line by line
print("\n\nDay 1 - Python Print Function")
print('The function is declared like this:')
print("print('what to print')")

# String concatenation
print("Hello" + " " + "Mani" + "!")

# ----------

# Debugging the code
# print(Day 1 - String Manipulation")
# print("String Concatenation is done with the "+" sign.")
#   print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")
print("\n\nDay 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# ----------

# Input function
print("\nHello" + " " + input("\n\nWhat is your name? ") + "!")

# ----------
# Exercise 3 - Input Function
var = input("\nWhat is your name? ")
print(len(var))

# ----------
# Exercise 4 - Variables
a = input("\n\nValue for a: ")
b = input("Value for b: ")
c = a
a = b
b = c
print("\na: " + a)
print("b: " + b)

# ----------
# Day 1 Project: Band Name Generator
#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line:
# Solution: https://replit.com/@appbrewery/band-name-generator-end

print("\n\nWelcome to the BAND NAME GENERATOR python program !!!")
city = input("What's the name of your city? ")
pet = input("What's the name of your pet? ")
print("\nYour band name is " + city + " " + pet + " !!!")

