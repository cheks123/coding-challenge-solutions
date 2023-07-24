import time
import math
t1 = time.perf_counter()
maxx = 0
limit = 80000
for i in range(100, int(math.sqrt(limit)) + 1):
    for k in range(i, 1000):
        m = i * k
        s = str(m)
        if m < limit and s == s[::-1]:
            maxx = max(maxx, m)
t2 = time.perf_counter()
print('**********************************************')

print(maxx)

print(t2 - t1, 'with array')
