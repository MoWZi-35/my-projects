#hello this is my py calculator
while True:
    num1 = int(input("write first number: "))
    op = input("write operation (+, -, *, /): ")
    num2 = int(input("write second number: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("You entered incorrect data.")
