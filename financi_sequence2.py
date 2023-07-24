def fibonacci(n):
    r = [0, 1]
    for i in range(n):
        r.append(r[i] + r[i+1])
    return r[:n]
    # return a list of fibonacci numbers

cube = lambda n: n ** 3

if __name__ == '__main__':
    n = 5
    print(list(map(cube, fibonacci(n))))
