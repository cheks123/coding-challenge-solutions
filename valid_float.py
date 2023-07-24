import re

for _ in range(int(input())):
    print(re.search(r'^([-\+])?\d*\.\d+$', input()) is not None)


'''
EXPLANATION
Start with - or +, followed by 0 or any number digits, followed by ., followed
by digits

Print True for float
Print False for non-float
'''
            
    
