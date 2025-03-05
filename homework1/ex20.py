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
num1 = abs(num1)
num2 = abs(num2)
div = num1 if (num1 < num2) else num2
while div > 0:
    if (num1 % div == 0 and num2 % div == 0):
        break
    div -= 1
print("div = ", div)
