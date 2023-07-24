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

print(noOfPairs(['bbcb', 'abccc', 'abc']))

print(noOfPairs(['aaaa', 'abba', 'ccc', 'caa', 'cbba', 'acaac', 'bcb']))
