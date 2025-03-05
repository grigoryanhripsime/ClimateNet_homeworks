str = input("Enter a string: ")
str = str.lower()
count = 0
for c in str:
    if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
        count += 1
print("count = ", count)
