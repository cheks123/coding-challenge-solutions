import math
'''
cinput = 1+2j
r = 2.23606797749979 
phase = 1.1071487177940904
'''
def complex1(k):
    r = ''
    i = ''
    c = ''
    for j in k:
        if j != ' ':
            c += j
    if c[0] != '-':
        if '-' in c:
            r, i = list(map(float, c[:-1].split('-')))
            i *= -1
        else:
            r, i = list(map(float, c[:-1].split('+')))

    if c[0] == '-':
        if '-' in c[1:]:
            r, i = list(map(float, c[1:][:-1].split('-')))
            i *= -1
            r *= -1
        else:
            r, i = list(map(float, c[1:][:-1].split('+')))
            r *= -1
    
    modulus = math.sqrt(r ** 2 + i ** 2)
    phase = math.atan(i/r)

    return modulus, phase * 180 / math.pi, r, i

print(math.atan.__doc__)
if __name__ == '__main__':
    print(complex1('2 + 3j'))
    print(complex1('2 - 3j'))
    print(complex1('-2 + 3j'))
    print(complex1('-2 - 3j'))
