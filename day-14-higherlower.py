from logohigherlower import logo
from logohigherlower import vs
from higherlowerdata import data
import random

score = 0
new_score = 0
game_over = "False"
old_score = 0

def random_dict_a():
    dict_a = random.choice(data)
    return dict_a

def random_dict_b():
    dict_b = random.choice(data)
    return dict_b


def check(answer, score, follower_a, follower_b):
    if answer == "A":
        if follower_a > follower_b:
            score += 1
            return score
        else:
            return "True"
    elif answer == "B":
        if follower_b > follower_a:
            score += 1
            return score
        else:
            return "True"


while game_over == "False":
    if new_score == 0:
        print(logo)
        print(f"Your score is: {new_score}")
    elif new_score == "True":
        # game_over = True
        print(f"\nIncorrect answer, your score is {old_score} see you later, bye!")
        break
    elif new_score > 0:
        print(logo)
        print(f"You're right, your score is: {new_score}")
        old_score = new_score   
    dict_a = random_dict_a()
    name_a = dict_a["name"]
    description_a = dict_a["description"]
    country_a = dict_a["country"]
    follower_a = dict_a["follower_count"]
# ----------
    dict_b = random_dict_b()
    name_b = dict_b["name"]
    description_b = dict_b["description"]
    country_b = dict_b["country"]
    follower_b = dict_b["follower_count"]
# ----------
    print(f"Compare A: {name_a}, {description_a}, from {country_a}")
    print(vs)
    print(f"Against B: {name_b}, {description_b}, from {country_b}")
    answer = input("Who has more followers? Type 'A' or 'B': ")
    new_score = check(answer, new_score, follower_a, follower_b)
