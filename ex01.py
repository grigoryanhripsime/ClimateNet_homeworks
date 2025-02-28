sum = 0

while True:
    choice = int(input("Enter a number(1 or 2): "))
    if choice == 1:
        num = int(input("Enter a number: "))
        sum += num
    elif choice == 2:
        print("sum = ", sum)
        break
    else:
        print("Invalid input!")
        
