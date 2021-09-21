#Import library
import random 

### User guess a random number ###
def guess(x):
    randomNumber = random.randint(1,x)

    guess = 0 # Set guess = 0 incase randomNumber == guess
    while guess != randomNumber:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        
        if guess < randomNumber:
            print("Too low. Guess again")
        elif guess > randomNumber:
            print("Too high. Guess again") 
    
    print(f"Congrats! You have guessed the number {randomNumber} correctly!")

### The computer guesses a user's number ###
def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c" and feedback != "C":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low #could also be high b/c low = high

        feedback = input(f"Is {guess} to high (H), too low (L), or correct (C)?")

        if feedback == "h" or feedback == "H":
            high = guess - 1

        if feedback == "l" or feedback == "L":
            low = guess + 1

    print(f"The computer guessed your number {guess} correctly!")

computer_guess(10)    