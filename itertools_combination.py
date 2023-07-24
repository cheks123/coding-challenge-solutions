from itertools import combinations
s, k = input().split(' ')
result = []
for i in range(1, int(k) + 1):
    result += sorted([''.join(sorted(x)) for x in list(combinations(s, i))])


print(*result, sep='\n')
