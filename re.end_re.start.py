import re

s = input()
k = input()
pattern = re.compile(k)
m = pattern.search(s)
if m:
    while m:
        print((m.start(), m.end() - 1))
        m = pattern.search(s, m.start() + 1)
else:
    print((-1, -1))
