n, m =  9, 27 #list(map(int, input().split(' ')))
j = 0
for i in range(n // 2):
    d = '.|.' * (i + 1 + j)
    print(d.center(m, '-'))
    j += 1

print('welcome'.center(m, '-'))

k = 2 * (n // 2) - 1

for i in range(n // 2):
    d = '.|.' * (k)
    print(d.center(m, '-'))
    k -= 2
