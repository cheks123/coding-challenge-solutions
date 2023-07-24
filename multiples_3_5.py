
import sys
import time

find_sum = lambda a, n: n * (2 * a + (n - 1) * a) // 2


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n3 = (n - 1) // 3
    n5 = (n - 1) // 5
    n15 = (n - 1) // 15
    print(find_sum(3, n3) + find_sum(5, n5) - find_sum(15, n15))

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5 ,
we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of  3 or  5 below N
'''
