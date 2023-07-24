# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
header = 'ID,MARKS,NAME,CLASS' #','.join(input().split())
Student = namedtuple('Student', header)

total = 0
for _ in range(n):
    record = Student(*input().split())
    total += int(record.MARKS)
    print(list(record))
print(total / n)

'''
5
ID MARKS NAME CLASS
1 97 JACK 9
2 50 STEV 8
5 55 HAV 7
4 77 KEN 10
3 88 UVO 5
73.4
'''
