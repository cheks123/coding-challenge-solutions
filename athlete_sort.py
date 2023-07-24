import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    length = len(arr)
    i = 0
    while i < length:
        j = 0
        while j < length - i - 1:
            if arr[j][k] > arr[j+1][k]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            j += 1
        i += 1
    
    for a in arr:
        print(' '.join([str(t) for t in a]))
