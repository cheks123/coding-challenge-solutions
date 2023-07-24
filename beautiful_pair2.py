from itertools import combinations
import time
def noOfPairs(box):
    r = combinations(box, 2)
    k = [''.join(t) for t in r]
    count = 0
    false = 0
    for i in k:
        s = set(i)
        odd = 0
        for g in s:
            if i.count(g) % 2 == 1:
                odd += 1
            if odd > 1:
                false += 1
                break
    return len(k) - false

t1 = time.perf_counter()
print(noOfPairs(['aaaa', 'abba', 'ccc', 'caa', 'cbba',
                 'acaac', 'bcb', 'abba', 'ccc', 'caa', 'cbba', 'acaac',
                 'bcb', 'abba', 'ccc', 'caa', 'cbba', 'acaac', 'bcb',
                 'abba', 'ccc', 'caa', 'cbba', 'acaac', 'bcb', 'abba',
                 'ccc', 'caa', 'cbba', 'acaac', 'bcb', 'abba', 'ccc',
                 'caa', 'cbba', 'acaac', 'bcb', 'abba', 'ccc', 'caa',
                 'cbba', 'acaac', 'bcb', 'abba', 'ccc', 'caa', 'cbba',
                 'acaac', 'bcb', 'abba', 'ccc', 'caa', 'cbba', 'acaac',
                 'bcb', 'abba', 'ccc', 'caa', 'cbba', 'acaac', 'bcb',
                 'abba', 'ccc', 'caa', 'cbba', 'acaac', 'bcb', 'abba',
                 'ccc', 'caa', 'cbba', 'acaac', 'bcb']))

print(noOfPairs(['aaaa', 'abba', 'ccc', 'caa', 'cbba', 'acaac', 'bcb']))
t2 = time.perf_counter()
print(t2 - t1)
'''
Geek love strings having atmost one character whose frequency is odd and
rest all (if exists) characters have even frequencies, he calls such
strings as beautiful strings. Geek has a box containing n strings.
You have to help him in counting number of pairs (i,j) (0<i<j<n-1)
such that a string formed by concatenating string at index i with
string at index j is a beautiful string. 

Note: Strings consist of only lowercase English letters.
'''
