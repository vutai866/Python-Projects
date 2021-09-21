import random

def play():
    print("R: Rock   P: Paper   S: Scissor")
    user = input("Your choice: ").lower()

    comp = random.choice(["r", "p", "s"])

    if user == comp:
        return "Tie"

    if winner(user, comp):
        return "You Won!"

    return "You lost!" 
    
    # r > s, s > p , p > r
def winner(user, comp):
    #return true if win
    if (user == "r" and comp == "s") or (user == "s" and comp == "p")\
        or (user == "p" and comp == "r"):
            return True

print(play())