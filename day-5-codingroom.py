# For loop
names = ["Steven", "Griffin", "Lois", "Chris", "Megan", "Brian", "Stewie"]
for name in names:
    print(name)

# ----------
# Average height
heights = input("\n\nEnter the students heights (Separate heights with spaces): ")
sep_heights = heights.split(" ")
sum = 0
count = 0
for i in sep_heights:
    sum += int(i)
    count += 1
print(f"The sum of heights is: {sum}")
avg = sum / count
float_avg = float(avg)
print(f"The average height is: {round(float_avg)}")

# ----------
# Exercise 2 - High Score
marks = input("\n\nEnter the students marks (Separate marks with spaces): ")
sep_marks = marks.split(" ")
value = 0
for mark in sep_marks:
    if int(mark) > value:
        value = int(mark)

print(f"The highest mark is: {value}")

# ----------
# Exercise 3 - Adding Even Numbers
sum = 0
for numbers in range(1, 101):
    if int(numbers) % 2 == 0:
        sum += numbers
print(f"The sum of even numbers between 1 and 100 is: {sum}")

# ----------
# Exercise 4 - FizzBuzz
for number in range(1, 101):
    if int(number) % 3 == 0 and int(number) % 5 == 0:
        print("FizzBuzz")
    elif int(number) % 3 == 0:
        print("Fizz")
    elif int(number) % 5 == 0:
        print("Buzz")
    else:
        print(number)

# ----------
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\n\nWelcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

char = nr_letters - nr_symbols - nr_numbers

letter_password = []
for i in range(1, char+1):
    letter = random.choice(letters)
    letter_password.append(letter)

symbol_password = []
for j in range(1, nr_symbols+1):
    symbol = random.choice(symbols)
    symbol_password.append(symbol)

number_password = []
for k in range(1, nr_numbers+1):
    number = random.choice(str(nr_numbers))
    number_password.append(number)

final_password = letter_password + symbol_password + number_password

string_final_password = ""
# # without randomness in final password
# print(string_final_password)

# with randomness in final password
final_passwords = random.sample(final_password, len(final_password))

for each in final_passwords:
    string_final_password += each

print(f"\nYour password can be: {string_final_password}")



