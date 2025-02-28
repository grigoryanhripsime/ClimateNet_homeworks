while True:
    try:
        num = int(input("num = "))
        if (num < 0):
            raise ValueError
        break
    except ValueError:
        print("Error")
sum = 0
while num > 0:
    sum += int(num % 10)
    num /= 10
print("sum = ", sum)
