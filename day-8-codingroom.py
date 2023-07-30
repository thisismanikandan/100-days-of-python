# # simple function
# def greet():
#     print("Hello world!")
#     print("Welcome to the new World")
#     print("Hey there!")

# # greet()

# # function with parameters
# def greet_with_name(name):
#     print(f"Hello {name}!")
#     print(f"How do you do, {name}?")

# greet_with_name("Manikandan")

# # functions with more than one input
# def greet_with(name, location):
#     print(f"Hi {name}, how are you?")
#     print(f"Do you still live in {location}?")

# greet_with("Mani", "Chennai")
# greet_with(location="Chennai", name="Mani")

# # Exercise 1 - Paint Area Calculator
# import math

# def calculation(height, width):
#     number_of_cans = (height*width)/5
    
#     print(f"\nYou'll need {math.ceil(number_of_cans)} can(s) of paint.")

# wall_height = float(input("\nEnter the height of wall: "))
# wall_width = float(input("Enter the width of wall: "))

# # calculation(wall_height, wall_width)

# # Exercise 2 - Prime Numbers
# def prime(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print(f"{number} is a prime number")
#     else:
#         print(f"{number} is a not a prime number")  

# number = int(input("\n\nEnter a number within 100: "))

# prime(number)

# Caesar's Cipher

from logocaesarcipher import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function block
def encrypt(message, shift_number):
    cipher = ""
    for position in range(len(message)):
        index = alphabet.index(message[position])
        cipher += alphabet[index+shift_number]
    print(f"The encoded message is {cipher}")

def decrypt(message, shift_number):
    cipher = ""
    for position in range(len(message)):
        index = alphabet.index(message[position])
        cipher += alphabet[index-shift_number]
    print(f"The decoded message is {cipher}")

# Main block
to_do = True
while to_do:
    to_do = input("\n\nType 'encode' to encrypt, type 'decode' to decrypt and 'quit' to end the game: ")
    if to_do == "quit":
        to_do = False
    elif to_do == "encode":
        message = input("Type your message: ")
        shift_number = int(input("Type your shift number: "))
        encrypt(message, shift_number)
    elif to_do == "decode":
        message = input("Type your message: ")
        shift_number = int(input("Type your shift number: "))
        decrypt(message, shift_number)



