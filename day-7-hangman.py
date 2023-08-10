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

# Importing random module
import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
end_of_game = False
lives = 6

# Testing
print(f"\n{chosen_word}")

# Creating blanks
word = []
for each_letter in chosen_word:
    word.append("_")

print(f"\n{word}")

# Guess logic
while not end_of_game:
    guess = input("\nEnter a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            word[position] = letter
    print(word)
           
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nYou lose :)")
    
    if "_" not in word:
        end_of_game = True
        print("\nYou win :)")

    print(stages[lives])