import time

print("Enter duration in seconds")
t = int(input(">>> "))
t1 = time.time()
while t:
        m, s = divmod(t, 60)
        print("{0}:{1}".format(m, s))
        time.sleep(1)
        t -= 1
t2 = time.time()
print('BLAST! BOOM!! BOOM!!!')
print(t2 - t1)
