def solution (n, ratings):
    r = {}
    count = {}
    for i in range(n):
        if ratings[i][0] in r:
            r[ratings[i][0]] = r[ratings[i][0]] + ratings[i][1]
        else:
            r[ratings[i][0]] = ratings[i][1]
        if ratings[i][0] in count:
            count[ratings[i][0]] += 1
        else:
            count[ratings[i][0]] = 1
    print(r)
    print(count)
    for k in r:
        r[k] = r[k]/count[k]
    print(r)
    
    maxx = 0
    maxx = max(r.values())
    print(maxx)

    result = []

    for i in  r:
        if r[i] == maxx:
            result.append(i)
    result.sort()
    return result[0]


if __name__ == '__main__':
    print(solution(4, [[512, 3], [123, 3], [987, 4], [123, 5]]))
