from itertools import product

k, m = list(map(int, input().split(' ')))
arr = [list(map(int, input().split(' ')))[1:] for _ in range(k)]
results = map(lambda x: sum(i ** 2 for i in x) % m, product(*arr))
print(max(results))
