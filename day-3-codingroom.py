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

# ----------
height = int(input("\n\nEnter your height: "))
age = int(input("Enter your age: "))
photo = input("Do you need photos? (yes/no): ")
if height >= 120:
    print("\nHurray! You can enjoy the rides!")
    if age >= 18:
        if photo == "yes":
            print("Please pay $15 for the rides and photos.")
        else:
            print("Please pay $12 for the rides.")
    elif age >= 12:
        if photo == "yes":
            print("Please pay $10 for the rides and photos.")
        else:
            print("Please pay $7 for the rides.")
    else:
        if photo == "yes":
            print("Please pay $8 for the rides and photos.")
        else:
            print("Please pay $5 for the rides.")
else:
    print("Sorry, you're not tall enough to take the rides :(")