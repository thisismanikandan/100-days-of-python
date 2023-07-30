# Grading exercise
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if int(student_scores[key]) > 90:
        student_grades[key] = "Outstanding"
    elif int(student_scores[key]) > 80:
        student_grades[key] = "Exceeds Expectations"
    elif int(student_scores[key]) > 70:
        student_grades[key] = "Acceptable"
    elif int(student_scores[key]) <70 :
        student_grades[key] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

# ----------
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

print(travel_log["Germany"][2])

# Remember - dicts can be nested within themselves
# dicts inside lists
# lists inside dicts

# ----------
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above
#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
    new_country = {}
    new_cities = []
    new_country["country"] = country
    new_country["visits"] = visits
    for city in cities:
        new_cities.append(city)
    new_country["cities"] = new_cities

    travel_log.append(new_country)

#🚨 Do not change the code below    
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# ----------------------------------------------------------------------------------------
# Please comment everything below to see the output for everything above this comment
# ----------------------------------------------------------------------------------------

# Blind Auction game

from hammerblindauction import logo
import os

os.system('cls')
print("Welcome to the secret auction program")

details_of_bidders = []

def new_bidder(name, value):
    bidder_details = {}
    bidder_details["Name"] = name
    bidder_details["Value"] = value
    details_of_bidders.append(bidder_details)

game_not_over = True

while game_not_over:
    print(logo)
    name = input("What is your name?: ")
    value = int(input("What's your bid?: "))
    new_bidder(name, value)
    move = input("Are there any other bidders? Type 'yes' or 'no' \n")
    os.system('cls')
    if move == "no":
        game_not_over = False

print(f"The bidders are: \n{details_of_bidders}")

# Value check logic
bid_value = []

for position in range(len(details_of_bidders)):
    bid_value.append(details_of_bidders[position]["Value"])

print(f"The bidded values are {bid_value}")

largest_bid = 0
# Actual check
for position in range(len(bid_value)):
    if bid_value[position] > largest_bid:
        largest_bid = bid_value[position]

print(f"The largest bid is {largest_bid}")

largest_bidder = ""
for position in range(len(details_of_bidders)):
    if details_of_bidders[position]["Value"] == largest_bid:
        largest_bidder = details_of_bidders[position]["Name"]

print(f"\nThe item is sold to {largest_bidder} for ${largest_bid}")
