import time
def largest_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return largest_prime(n // i)
    return n


if __name__ == '__main__':
    t1 = time.perf_counter()
    print(largest_prime(131957788))
    t2 = time.perf_counter()
    print(t2 - t1, 'without math.sqrt' )
