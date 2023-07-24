import re
n = '100,000,000.000'
print(*re.split(',|\.', n), sep='\n')
