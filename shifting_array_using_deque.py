from collections import deque
t = int(input())
for i in range(t):
    n, steps = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))
    d = deque(arr)
    for j in range(steps):
        d.appendleft(d[-1])
        d.pop()
    print(*d, sep=' ')


'''
Shifting array using deque
[1, 2, 3, 4, 5] -> [5, 1, 2, 3, 4] -> [4, 5, 1, 2, 3] -> [3, 4, 5, 1, 2]
'''
