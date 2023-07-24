n = 10000
a = 0
b = 1
summ = 0
while a + b <= n:
    a, b = b, a+b
    if b%2==0:
        summ += b
    print(b)
print(summ)

'''find the sum of even numbers in the fibonnaci sequence up to n'''
