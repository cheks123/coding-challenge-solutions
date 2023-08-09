def beautifulNumber(n : int) -> bool:
        r = []
        s = str(n)
        t = True
        while t:
            summ = 0
            for i in s:
                summ += int(i) ** 2
            if summ == 1:
                return 1
            t = summ not in r
            s = str(summ)
            if t:
                r.append(summ)
            else:
                return 0


print(beautifulNumber(2))
