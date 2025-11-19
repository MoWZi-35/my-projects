import random

print("---Welcome to Game---")
print("-Guess The Number-")
print("chose complexity of game")
print("easy 1-3 numbers")
print("normal 1-10 numbers")
print("hard 1-15 numbers")
print("your complexity 1-your numbers")

def play(complex):
    num = random.randint(1, complex)
    while True:
        try:
            player = int(input(f"enter number 1 - {complex}: "))
            if 1 <= player <= complex:
                break
            else:
                print(f"ERROR. number must be between 1 and {complex}")
        except ValueError:
            print("ERROR. please write valid number")
    
    if player == num:
        print("you won")
    else:
        print("you lose, the correct number is: ", num)

def contin():
    while True:
        con = input("do you want continue the game? y/n: ")

        if con == "y":
            return True
        elif con == "n":
            return False
        else:
            print("ERROR. please write only 'y' or 'n'")

while True:
    try:
        complex = int(input("write complexity = 3 / 5 / 15 / your number: "))
        if complex > 0:
            play(complex)

            if not contin():
                print("thanks for playing")
                break
        else:
            print("ERROR. Complexity must be positive number!")
    except ValueError:
        print("ERROR. please write valid number")
    
