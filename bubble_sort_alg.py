arr = [6, 4, 10, 8, 21, 17, 1, 13, 9, 11, 20, 19, 5, 18]
length = len(arr)
i = 0
print(arr)

while i < length:
    j = 0
    while j < length - i - 1:
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
        j += 1
    i += 1
print(arr)
