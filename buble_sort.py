print("--- Bubble Sort ---")
while True:
    print("enter 6 nubers you want to sort:")
    n1 = float(input("first number: "))
    n2 = float(input("second number: "))
    n3 = float(input("third number: "))
    n4 = float(input("fourth number: "))
    n5 = float(input("fifth number: "))
    n6 = float(input("sixth number: "))
    print("if you want to sort numbers from smallest to highest enter: 1")
    print("if you want to sort numbers from highest to smallest enter: 2")
    choice = int(input("enter your answer: "))


    def sort():
        global n1, n2, n3, n4, n5, n6
        if n1 > n2:
            n1, n2 = n2, n1
            sort()
        if n2 > n3:
            n2, n3 = n3, n2
            sort()
        if n3 > n4:
            n3, n4 = n4, n3
            sort()
        if n4 > n5:
            n4, n5 = n5, n4
            sort()
        if n5 > n6:
            n5, n6 = n6, n5
            sort()

    def sort2():
        global n1, n2, n3, n4, n5, n6
        if n1 < n2:
            n1, n2 = n2, n1
            sort2()
        if n2 < n3:
            n2, n3 = n3, n2
            sort2()
        if n3 < n4:
            n3, n4 = n4, n3
            sort2()
        if n4 < n5:
            n4, n5 = n5, n4
            sort2()
        if n5 < n6:
            n5, n6 = n6, n5
            sort2()

    if choice == 1:
        sort()
    elif choice == 2:
        sort2()

    print("sorted: ", n1, "/", n2, "/", n3, "/", n4, "/", n5, "/", n6)
    choice2 = input("do you want to sort again? y/n: ")
    if choice2 == "y":
        None
    elif choice2 == "n":
        exit()