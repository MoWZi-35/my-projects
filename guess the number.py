import random

print("---Welcome to Game---")
print("-Guess The Number-")

while True:
    print("-Now please chose game complexity-")
    print("1. easy (1-3 numbers)")
    print("2. normal (1-10 numebrs)")
    print("3. hard (1-15 numbers)")
    complexity = int(input("please enter complexity 1/2/3 : "))

    if complexity == 1:
        num = random.randint(1, 3)
        player = int(input("enter the number you think is correct: "))
        if player == num:
            print("Congratulations, you won.")
        else:
            print("Sorry, you didn't guess the correct number. correct number: ", num)
        next = input("do you want play again y/n: ")
        if next == "y":
            None
        elif next == "n":
            break
   
    if complexity == 2:
        num = random.randint(1, 10)
        player = int(input("enter the number you think is correct: "))
        if player == num:
            print("Congratulations, you won.")
        else:
            print("Sorry, you didn't guess the correct number. correct number: ", num)
        next = input("do you want play again y/n: ")
        if next == "y":
            None
        elif next == "n":
            break

    if complexity == 3:
        num = random.randint(1, 15)
        player = int(input("enter the number you think is correct: "))
        if player == num:
            print("Congratulations, you won.")
        else:
            print("Sorry, you didn't guess the correct number. correct number: ", num)
        next = input("do you want play again y/n: ")
        if next == "y":
            None
        elif next == "n":
            break

