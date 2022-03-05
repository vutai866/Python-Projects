# Author: Tai Vu
# Program: Hangman game (version: countries) 
# #

import random
import string
from countries import countries

def get_word(countries):

    # Randomly choose a word in list
    word = random.choice(countries)

    while "-" in word or " " in word:
        word = random.choice(countries)

    return word.upper()

def hangman():
    word = get_word(countries)
    wordLetter = set(word)  #Letters in word
    alphabet = set(string.ascii_uppercase)
    usedLetter = set() # User has guessed letters

    LIVES = 6 #Number of lives

    # Getting user input
    while len(wordLetter) > 0 and LIVES > 0:
        #Letters used. join(["a", "b", "cd"]) --> "a b cd"
        print("You have : ", LIVES, " lives left.")
        print("You have used these letters: ", " ".join(usedLetter))
    
        #Current words
        wordList = [letter if letter in usedLetter else "-" for letter in word]
        print("Current words: ", " ".join(wordList))
        print("--------------------------")

        userLetter = input("Guess a letter: ").upper()
        if userLetter in alphabet - usedLetter:
            usedLetter.add(userLetter)
            if userLetter in wordLetter:
                wordLetter.remove(userLetter)
            
            else:
                LIVES -= 1 #Take away 1 live if wrong 
                print("Letter is not in word.")

        elif userLetter in usedLetter:
            print("You already used that character. Try again!")

        else:
            print("Invalid character. Please try again.")

    if LIVES == 0:
        print("You died. Sorry. The word was: ", word)
    else:
        print("You guessed the word ", word, "!!")

hangman()