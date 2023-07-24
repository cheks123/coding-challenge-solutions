import re

txt = 'Sorting1234'

import re

lower = upper = odd = even = ''
for s in txt:
    if re.search(r'[a-z]', s):
        lower += s
    if re.search(r'[A-Z]', s):
        upper += s
    if re.search(r'\d', s):
        if int(s) % 2 != 0:
            odd += s
        else:
            even += s
print(''.join(sorted(lower)+sorted(upper)+ sorted(odd) + sorted(even)))
