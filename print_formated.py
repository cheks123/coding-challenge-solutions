def print_formatted(number):
    result = []
    for i in range(number):
        n = i + 1
        b = ''
        while n != 0:
            t = n % 2
            n = n // 2
            b += str(t)
        
        o = ''
        
        n = i + 1
        while n != 0:
            t = n % 8
            n = n // 8
            o += str(t)
        
        n = i + 1
        h = ''
        hexd = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        while n != 0:
            t = n % 16
            n = n // 16
            if t > 9:
                h += hexd[t]
                continue
            h += str(t)
        result.append([b[::-1], o[::-1], h[::-1]])
        
    p = 1
    r = len(result[-1][0])
    for i in result:
        print(str(p).rjust(r, ' '), i[1].rjust(r, ' '), i[2].rjust(r, ' '), i[0].rjust(r, ' '))
        p += 1


print_formatted(17)
