n, x = list(map(int, input().split(' ')))

arr = []
for _ in range(x):
    row = list(map(float, input().split(' ')))
    arr.append(row)

combine = zip(*arr)

for i in combine:
    print(sum(i) / x)

'''
>>>input
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
'''
