arr = [1, 2, 3, 4, -1, 4]
max_val = max(arr)
while max_val in arr:
    arr.remove(max_val)
print("second largest: ", max(arr))
