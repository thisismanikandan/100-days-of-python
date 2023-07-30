# BlackJack

import random
import os
from logoblackjack import logo
os.system('cls')
print(logo)

overall_game = True

while overall_game:
    choice = input("\n\nDo you want to play BlackJack? (yes or no): ")
    os.system('cls')
    print(logo)
    if choice == "yes":
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        your_cards = []
        computer_cards = []

        your_cards.append(random.choice(cards))
        your_cards.append(random.choice(cards))
        print(your_cards)

        computer_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        print(computer_cards[0])

        choice = input("Type 'y' to get another card, type 'n' to pass: ")

        game_on = True

        def hit():
            your_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))

        def redo_hit():
            your_cards.pop()
            computer_cards.pop()
            your_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))

        def sum():
            your_cards_sum = 0
            for each in your_cards:
                your_cards_sum += each
            return your_cards_sum

        def comp_sum():
            comp_cards_sum = 0
            for each in computer_cards:
                comp_cards_sum += each
            return comp_cards_sum

        def check_with_21(your_sum, computer_sum):
            print(f"Your sum is {your_sum} and computer sum is {computer_sum}")
            if your_sum > 21 and computer_sum > 21:
                print("\nYou lose!!!")
                return
            elif your_sum > 21:
                print("\nComputer wins!!!")
                return
            elif computer_sum > 21:
                print("\nYou win!!!")
                return
            elif your_sum == computer_sum:
                redo_hit()
                return
            your_diff = 21 - your_sum
            comp_diff = 21 - computer_sum
            print(f"Your diff is {your_diff} and computer diff is {comp_diff}")
            if your_diff > 21:
                print("\nComputer wins!!!")
            elif comp_diff > 21:
                print("\nYou win!!!")
            elif your_diff < comp_diff:
                print("\nYou win!!!")
            elif comp_diff < your_diff:
                print("\nComputer wins!!!")

        while game_on:   
            if choice == "y":
                hit()
                your_sum = sum()
                computer_sum = comp_sum()
                print(your_cards, computer_cards)
                print(your_sum, computer_sum)
                check_with_21(your_sum, computer_sum)
            if choice == "n":
                your_sum = sum()
                computer_sum = comp_sum()
                print(your_cards, computer_cards)
                print(your_sum, computer_sum)
                check_with_21(your_sum, computer_sum)
            game_on = False
            print("\nThanks for playing!!!")

    else:
        print("Bubbye!")
        overall_game = False
