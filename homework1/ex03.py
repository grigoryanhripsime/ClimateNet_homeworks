while True:
    while True:
        op = input("Enter the operation: ")
        if op == '+' or op == '-' or op == '*' or op == '/':
            break
        elif op == '5':
            exit()
        else:
            print("Invalid input!")
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input")
    while True:
        try:
            num2 = int(input("Enter the second number: "))
            if (op == '/' and num2 == 0):
                print("Can't divide to 0!")
                continue
            break
        except ValueError:
            print("Invalid input")
    match op:
        case "+":
            print("num1 + num2 = ", num1+num2)
        case "-":
            print("num1 - num2 = ", num1-num2)
        case "*":
            print("num1 * num2 = ", num1*num2)
        case "/":
            print("num1 / num2 = ", num1/num2)
