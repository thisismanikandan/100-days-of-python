# ----------
# Testing subscripting
print("Hello"[4])
print("123" + "456")

# Integers
print(123+345)
print(567_789+847_000)  # _ will be ignored and can be used for visual identification

# Float
print(123.234)

# Boolean
print(True)
print(False)

# use str() method to convert integers to string
count = len(input("\nWhat's your name? "))
print(type(count))
new_count = str(count)
print("Your name has " + new_count + " characters")

# use float() method to convert integer to float
print(170 + float("9.004"))

# Exercise 1 - Data Types
number = input("\nEnter a 2 digit number: ")
print(type(number))
sum = int(number[0]) + int(number[1])
print(sum) 

# BMI calculator
weight = input("\nEnter your weight in kg(s): ")
height = input("Enter your height in metre(s): ")
# print(type(weight))
# print(type(weight))
weight_in_float = float(weight)
height_in_float = float(height)
BMI = (weight_in_float)/((height_in_float)*(height_in_float))
print(int(BMI))

# Round method round(3/2,2) round to 2 digit after decimal
# Flow division // - returns just the integers cutiting off the decimals
# f-string f"Your score is {score}"
 
# Your life in weeks
print("\nWelcom to age calculator")
age = float(input(("Your age in years: ")))
years = 90 - age
months = int(years*12)
weeks = int(years*52)
days = int(years*365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# Tip calculator

print("\nWELCOME to the TIP calculator")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_tip = bill + ( bill * (tip/100) )

split = round((bill_tip / people), 2)

print(f"Each person should pay: ${split}")