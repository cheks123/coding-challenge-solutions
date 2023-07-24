from time import perf_counter
def noOfPairs(box):
    false = 0
    r = []
    for i in range(len(box)):
        for k in box[i+1:]:
            r.append(box[i]+k)
    for a in r:
        odd = 0
        for t in set(a):
            if a.count(t) % 2 == 1:
                odd += 1
            if odd > 1:
                false += 1
                break
    return len(r) - false

t1 = perf_counter()
print(noOfPairs(['bbcb', 'abccc', 'abc']))

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
t2 = perf_counter()
print(t2 - t1, 'no comb')

'''
Geek love strings having atmost one character whose frequency is odd and
rest all (if exists) characters have even frequencies, he calls such
strings as beautiful strings. Geek has a box containing n strings.
You have to help him in counting number of pairs (i,j) (0<i<j<n-1)
such that a string formed by concatenating string at index i with
string at index j is a beautiful string. 

Note: Strings consist of only lowercase English letters.
'''
