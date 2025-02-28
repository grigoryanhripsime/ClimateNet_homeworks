while True:
    try:
        n = int(input("n = "))
        if (n <= 0):
            raise ValueError()
        break
    except ValueError:
        print("Error")
a, b = 0, 1

for i in range(1, n + 1):
    print(a, end=' ')
    a, b = b, a + b
print()
