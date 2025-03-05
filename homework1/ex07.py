while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Input Error")
            
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
