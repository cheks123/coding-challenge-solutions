import time


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum(range(0, n, 3)) + sum(range(0, n, 5)) - sum(range(0, n, 15)))



t1 = time.perf_counter()
n = 1000000
print(sum(range(0, n, 3)) + sum(range(0, n, 5)) - sum(range(0, n, 15)))
t2 = time.perf_counter()
print(t2 - t1)
