def alph_rhombus(size):
    alph = list('abcdefghijklmnopqrstuvwxyz')
    start = alph[:size]
    length = len(start)

    kk = []
    for i in range(size):
        r = start[-1-i:]
        k = '-'.join(r[1:][::-1] + r)
        kk.append(k)
        print(k.center(4* size - 3, '-'))

    for i in kk[:-1][::-1]:
        print(i.center(4* size - 3, '-'))

if __name__ == '__main__':
    alph_rhombus(10)
    
