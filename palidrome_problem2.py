import time
t1 = time.perf_counter()
maxx = 0
for i in range(100, 1000):
    for k in range(100, 1000):
        m = i * k
        s = str(m)
        if s == s[::-1]:
            maxx = max(maxx, m)

print(maxx)
t2 = time.perf_counter()
print(t2 - t1, 'without arr')
