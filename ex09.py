import math

while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input!")
for i in range(2, int(math.sqrt(num)) + 1):
    if (num % i == 0):
        print("The number is not prime!")
        exit()
print("The number is prime!")
