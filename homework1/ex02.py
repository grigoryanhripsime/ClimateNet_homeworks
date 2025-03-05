

while True:
    while True:
        try: 
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("invalid input")
    if num == 0:
        break
    if num % 2 == 0:
        print("The number is even!")
    else:
        print("The number is odd!")
