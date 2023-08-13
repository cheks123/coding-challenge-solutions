def nthFibonacci(n : int) -> int:
        arr = [0]*(n+1)
        arr[1] = 1
        for i in range(2,n+1):
            arr[i] = arr[i-2] + arr[i - 1]
        return arr[n]
        # code here

print(nthFibonacci(10000))
