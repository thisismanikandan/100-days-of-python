# Leap year with function
def is_leap(year):
  """Checks if the year is a leap year or not"""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  """Checks if the year is leap and if month is 2 if so return 29"""
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year):
      if month == 2:
        return 29
  return month_days[month-1]

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# ----------
# Calculator
import os
from logocalculator import logo
print(logo)

calc_number = 1
still_calculating = True

# Defining functions
def addition(first_number, second_number):
    return first_number + second_number

def subtraction(first_number, second_number):
    return first_number - second_number

def multiplication(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    return first_number / second_number

def operation(first_number):
    operator = input("\nPick an operation: ")
    second_number = float(input("What's the next number?: "))
    if operator == "+":
        result = addition(first_number, second_number)
        print(f"The sum is {result}")
        return result
    elif operator == "-":
        result = subtraction(first_number, second_number)
        print(f"The remainder is {result}")
        return result
    elif operator == "*":
        result = multiplication(first_number, second_number)
        print(f"The product is {result}")
        return result
    elif operator == "/":
        result = division(first_number, second_number)
        print(f"The quotient is {result}")
        return result
    
os.system('cls')

# Logic starts
print(logo)
first_number = float(input("What's the first number?: "))
print("\n+\n-\n*\n/")
value = operation(first_number)

# Continuity logic
check_is = True
while check_is:
        check = input(f"Type 'y' to continue calculating with {value}, or type 'n' to start a new calculation or type 'q' to quit: ")
        if check == "y":
            first_number = value
            value = operation(first_number)
        elif check == "n":
            os.system('cls')
            print(logo)
            first_number = float(input("What's the first number?: "))
            print("\n+\n-\n*\n/")
            value = operation(first_number)
        elif check == "q":
            print("\nSee you next time, bubbye !!!")
            check_is = False




