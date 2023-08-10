from game_data import data
from logohigherlower import logo, vs
import random
import os

score = 0

def separate(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check(follower_count_A, follower_count_B, guess):
    if follower_count_A < follower_count_B:
        if guess == "A":
            return False
        else:
            return True
    else:
        if guess == "A":
            return True
        else:
            return False

continue_flag = True

account_B = random.choice(data)

while continue_flag:
    account_A = account_B
    account_B = random.choice(data)

    while account_A == account_B:
        account_B = random.choice(data)

    print(logo)
    print(f"Compare A: {separate(account_A)}")
    print(vs)
    print(f"Compare B: {separate(account_B)}")

    guess = input("Who has more followers? Type 'A' or 'B': ")
    follower_count_A = account_A["follower_count"]
    follower_count_B = account_B["follower_count"]

    is_correct = check(follower_count_A, follower_count_B, guess)
    os.system('cls')

    if is_correct == True:
        score += 1
        print(f"You're right, your score is {score}")
        
    else:
        print(f"You're wrong and your final score is {score}")
        continue_flag = False





