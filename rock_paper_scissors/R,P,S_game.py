import random
choices = ['r', 'p', 's']

print("---Welcome to game rock, paper, scissors---")

def game():
    while True:
        player = input("please enter your choice: rock-r, paper-p, scissors-s.: ").lower()
        if player in choices:
            break
        else:
            print("please enter only first letter of your choice (r, p, s).")
        
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("Draw!")
    elif (player == "r" and computer == "s") or \
         (player == "p" and computer == "r") or \
         (player == "s" and computer == "p"):
        print("You won!")
    else:
        print("You lose!")

def ask_continue():
    while True:
        con = input("Do you want to continue game? y/n: ").lower()
        if con == "y":
            return True
        elif con == "n":
            return False
        else:
            print("Please enter y or n.")

while True:
    game()
    if not ask_continue():
        print("Thanks for playing! Goodbye!")
        break
