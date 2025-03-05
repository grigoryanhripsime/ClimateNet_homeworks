while True:
    summary = 0
    try:
        str1 = input("List separated by spaces: ")
        str1_list = str1.split()
        for i in str1_list:
            summary += int(i)
        break
    except ValueError:
        print("Error")
print("Summary = ", summary)
