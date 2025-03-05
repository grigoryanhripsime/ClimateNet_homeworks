while True:
    try:
        num1 = int(input("num1 = "))
        break
    except ValueError:
        print("Error")
while True:
    try:
        num2 = int(input("num2 = "))
        break
    except ValueError:
        print("Error")
while True:
    try:
        num3 = int(input("num3 = "))
        break
    except ValueError:
        print("Error")
if (num1 >= num2 and num1 >= num2):
    print(num1)
elif(num2 >= num1 and num2 >= num3):
    print(num2)
else:
    print(num3)
