import random

count = 0

num = random.randint(1, 10)
while True:
    try:
        choice = int(input("Enter a number: "))
        count += 1
        if num == choice:
            break
        elif num > choice:
            print("Number is bigger!")
        else:
            print("Number is smaller!")
    except ValueError:
        print("Invalid input!")
print("Number of attempts: ", count)
