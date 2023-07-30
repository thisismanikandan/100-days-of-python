# Greetings to Hangman game
print("\n\nWelcome to Hangman!!!")

# Stages
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random

words_list = ["hello", "welcome", "world"]
display = []
chosen_word = random.choice(words_list)
print(f"Chosen word is: {chosen_word}")

for letter in chosen_word:
    display += "_"
    
print(display)

end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Enter a letter: ")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = guess
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose")
            end_of_game = True
    
    if "_" not in display:
        end_of_game = True
        print("You won")

    print(stages[lives])
