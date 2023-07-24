import time
t1 = time.perf_counter()
n = 10
arr = []
for k in range(2, n + 1):
    arr.append(k)
length = len(arr)
for i in range(length):
    t = arr[i]
    for j in range(i + 1, length):
        if arr[j] % t == 0:
            arr[j] = arr[j] // t
    print(arr)

m = 1
for n in arr:
    m *= n
t2 = time.perf_counter()

print(m)
print(t2 - t1)
