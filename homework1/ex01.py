sum1 = 0

while True:
    while True:
        try:
            choice = int(input("Enter a number(1 or 2): "))
            break
        except ValueError:
            print("invalid input")
    if choice == 1:
        while True:
            try:
                num = int(input("Enter a number: "))
                break
            except ValueError:
                print("invalid input")
        sum1 += num
    elif choice == 2:
        print("sum = ", sum1)
        break
    else:
        print("Invalid input!")
        
