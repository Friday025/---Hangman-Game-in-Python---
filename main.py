# to do import necessary libraries for this project

import random
from words import words
from hangman_art import logo , stages

print(logo)

# to do randomly select a word from words.py and get the length of that word 
# This block of code is implementing a simple hangman game in Python. Here's a breakdown of what it
# does:
lives = 6
is_game = True
while is_game :

    selection = random.choice(words)
    word_length = len(selection)

    # Create a display list to show the guessed letters
    display = ["_" for _ in range(word_length)]

    print("_".join(display)) 

    # to do:- take user input and check that the word is match is the selection word 

   # This block of code is responsible for taking user input to guess a word in a simple hangman game
   # implementation. Here's a breakdown of what it does:
    print(selection[:-2],"_ _")
    guess = input("Guess a word : ")

    # check if word is already in the selection
    if guess in display:
        print(f"You've already guessed {guess}")
    

    # check if guess is in selection 

    if guess == selection:
        print(f"You're guess word {guess} is correct ")
    
    if guess != selection:
        print(f"You're guessed word is incorrect the correct word is {selection}")
        lives -= 1
        print(stages[lives])
        print(f"You have left {lives} chance to contiune.")
        if lives == 0:
            is_game = False
            print(f"You lose the word is {selection}")