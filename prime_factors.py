def primeFactors(n):
    result = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            result.append(i)
            n = n // i
    if n > 1:
            result.append(n)
    return result


print(primeFactors(180))
