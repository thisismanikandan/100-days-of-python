# # odd or even
# num = int(input("\nEnter a number: "))
# if num % 2 == 0:
#     print(f"{num} is an even number !")
# else:
#     print(f"{num} is an odd number !")

# # ----------
# height = int(input("\n\nEnter your height: "))
# age = int(input("Enter your age: "))

# if height >= 120:
#     print("\nHurray! You can enjoy the rides!")
#     if age >= 18:
#         print("Please pay $12 for the rides.")
#     elif age >= 12:
#         print("Please pay $7 for the rides.")
#     else:
#         print("Please pay $5 for the rides.")
# else:
#     print("Sorry, you're not tall enough to take the rides :(")

# # ----------
# # BMI calculator v2.0
# weight = input("\nEnter your weight in kg(s): ")
# height = input("Enter your height in metre(s): ")
# # print(type(weight))
# # print(type(weight))
# weight_in_float = float(weight)
# height_in_float = float(height)
# BMI = (weight_in_float)/((height_in_float)*(height_in_float))
# float_BMI = float(BMI)
# float_BMI = round(float_BMI, 1)
# if float_BMI >= 35:
#     print(f"\nYour BMI is {float_BMI}, you are clinically obese")
# elif float_BMI >= 30:
#     print(f"\nYour BMI is {float_BMI}, you are obese")
# elif float_BMI >= 25:
#     print(f"\nYour BMI is {float_BMI}, you are slightly overweight")
# elif float_BMI >= 18.5:
#     print(f"\nYour BMI is {float_BMI}, you are in normal weight")
# else:
#     print(f"\nYour BMI is {float_BMI}, you are underweight")    

# # ----------
# # Leap year
# year = int(input("\n\nEnter the year: "))
# if year % 4 == 0:
#     if year %100 == 0:
#         if year %400 == 0:
#             print(f"The year {year}, is a leap year")
#         else:
#             print(f"The year {year}, is not a leap year")
#     else:
#         print(f"The year {year}, is a leap year")
# else:
#     print(f"The year {year}, is not a leap year")

# # ----------
# height = int(input("\n\nEnter your height: "))
# age = int(input("Enter your age: "))
# photo = input("Do you need photos? (yes/no): ")
# if height >= 120:
#     print("\nHurray! You can enjoy the rides!")
#     if age >= 18:
#         if photo == "yes":
#             print("Please pay $15 for the rides and photos.")
#         else:
#             print("Please pay $12 for the rides.")
#     elif age >= 12:
#         if photo == "yes":
#             print("Please pay $10 for the rides and photos.")
#         else:
#             print("Please pay $7 for the rides.")
#     else:
#         if photo == "yes":
#             print("Please pay $8 for the rides and photos.")
#         else:
#             print("Please pay $5 for the rides.")
# else:
#     print("Sorry, you're not tall enough to take the rides :(")

# # ----------
# # pizza order program
# print("\n\nHere's our price list:\nSmall Pizza: $15\nMedium Pizza: $20\nLarge Pizza: $25\nPepperoni for Small Pizza: +$2\nPepperoni for Medium or Large Pizza: +$3\nExtra cheese for any size pizza: + $1")
# size = input("\nEnter your pizza size (L or M or S): ")
# pep = input("Do you want to add pepperoni? (Y or N): ")
# cheese = input("Do you want extra cheese? (Y or N): ")
# if size == "L":
#     bill = 25
#     if pep == "Y":
#         bill += 3
#         if cheese == "Y":
#             bill += 1
#             print(f"Your final bill is: ${bill}")
#         else:
#             print(f"Your final bill is: ${bill}")
#     else:
#         print(f"Your final bill is: ${bill}")
# elif size == "M":
#     bill = 20
#     if pep == "Y":
#         bill += 3
#         if cheese == "Y":
#             bill += 1
#             print(f"Your final bill is: ${bill}")
#         else:
#             print(f"Your final bill is: ${bill}")
#     else:
#         print(f"Your final bill is: ${bill}")
# elif size == "S":
#     bill = 15
#     if pep == "Y":
#         bill += 2
#         if cheese == "Y":
#             bill += 1
#             print(f"Your final bill is: ${bill}")
#         else:
#             print(f"Your final bill is: ${bill}")
#     else:
#         print(f"Your final bill is: ${bill}")

# # ----------
# # Love calculator
# name1 = input("\n\nEnter your name: ")
# name2 = input("Enter your partner's name: ")
# name = name1 + name2
# name = name.lower()
# # Checking TRUE
# t = name.count('t')
# r = name.count('r') 
# u = name.count('u') 
# e = name.count('e')
# true_count = t + r + u + e
# print(f"True count = {true_count}")
# # Checking Love
# l = name.count('l')
# o = name.count('o')
# v = name.count('v')
# e = name.count('e')
# love_count = l + o + v + e
# print(f"Love count = {love_count}")
# value = str(true_count) + str(love_count)
# print(f"Value is {value}")
# value = int(value)
# if value < 10 or value > 90:
#     print(f"Your score is {value}, you go together like coke and mentos.")
# elif value >= 40 and value <= 51:
#     print(f"Your score is {value}, you are alright together.")
# else:
#     print(f"Your score is {value}")

# # ----------
# print('''
#         ____________________________________________________________________
#  / \-----     ---------  -----------     -------------- ------    ----\\
#  \_/__________________________________________________________________/
#  |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
#  |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
#  | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
#  |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
#  |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
#  |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
#  |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
#  |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
#  | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
#  |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
#  |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
#  | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
#  |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
#  | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
#  |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
#  | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
#  |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
#  | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
#  |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
#  |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
#  / \----- ----- ------------  ------- ----- -------  --------  -------\\
#  \_/_______________________________________________________________
#       ''')

# print("\nWelcome to the Treasure Island !!!")
# print("Your mission is to find the treasure")
# start = input("How do you want to start? (left or right): ")
# if start == "left":
#     next = input("Do you want to swim or wait? (swim or wait): ")
#     if next == "wait":
#         third = input("Which door? (red, yellow or blue): ")
#         if third == "yellow":
#             print("You won !!!")
#         elif third == "red":
#             print("Burned by fire...\nGame over !!!")
#         elif third == "blue":
#             print("Eaten by beasts...\nGame over !!!")
#     else:
#         print("Attacked by trouts...\nGame over !!!")
# else:
#     print("Fall into a hole...\nGame over !!!")