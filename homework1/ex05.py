def factorial(num):
    if (num == 0):
        return 0
    if (num == 1):
        return 1
    return num * factorial(num - 1)

while True:
    try:
        num = int(input("Enter a number: "))
        if (num < 0):
            raise ValueError()
        else:
            print(factorial(num))
            break
    except ValueError:
        print("Invalid input")
