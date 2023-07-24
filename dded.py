'''p = [1]
s = {1}
t = 0
moves ='FFFF'
for i in moves:
    if i == 'F':
        t = p[-1] + 1
    if i == 'B':
        t = p[-1] - 1
    p.append(t)
    s.add(t)
print(len(s))


edges[][] = [[1, 5, 3],
             [2, 5, 3],
             [1, 4, 2],
             [5, 3, 2]]
'''

trackLength = 23
m = 3
#spells = [1, 5, 9]
spells = [3, 4, 5, 6, 9, 11, 16, 18, 19, 25]

summ = sum(spells)
mi = min(spells)
d = 0
k = 0
n = 0
while d < trackLength:
    d = 0
    k += 1
    for i in range(mi, summ + k + 1):
        if i in spells:
            n = k
        if n > 0:
            d += n
            n -= 1
    
        if d >= trackLength:
            break
print(k)
        
