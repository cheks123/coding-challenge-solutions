s = input()
arr = []
for i in set(s):
    arr.append([i, s.count(i)])
length = len(arr)
i = 0
while i < length:
    j = 0
    while j < length - i - 1:
        if arr[j][1] < arr[j + 1][1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if arr[j][1] == arr[j + 1][1]:
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    
        j += 1
    i += 1
for n in range(3):
    print(*arr[n])
