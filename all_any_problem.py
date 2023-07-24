n, arr = int(input()), input().split()
print(all([int(i) > 0 for i in arr]) and any([k == k[::-1] for k in arr]))
