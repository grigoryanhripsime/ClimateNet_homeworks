while True:
    try:
        str1 = input("Enter a number: ")
        num = int(str1)
        if (num < 0)
            raise ValueError()
        count = len(str1)
        break
    except ValueError:
        print("Error")

new_num = 0
for c in str1:
    new_num += int(c) ** count
if (num == new_num):
    print("Armstrong!")
else:
    print("Not armstrong!")
