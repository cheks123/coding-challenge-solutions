import re
m = re.findall(r'([A-Za-z0-9])\1+', input())
if m:
    print(m[0])
else:
    print(-1)

'''
Regular expression to find repeated characters in a string.
'''
