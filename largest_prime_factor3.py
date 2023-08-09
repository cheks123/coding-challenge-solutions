def largestPrimeFactor (N):
        prime_factors = []
        i = 2
        while i * i <= N:
            if N % i != 0:
                i += 1
            else:
                N //= i
                prime_factors.append(i)
        if N > 1:
            prime_factors.append(N)
        
        largest_prime_factor = max(prime_factors)
        print(prime_factors)
        return largest_prime_factor

print(largestPrimeFactor(131957788))
