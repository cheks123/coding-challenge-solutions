for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    length = len(arr)
    result = []
    left = 0
    right = -1
    yes = True
    for i in range(length):
        if arr[left] > arr[right]:
            result.append(arr[left])
            left += 1
            if len(result) > 1:
                if result[-1] > result[-2]:
                    print('No')
                    yes = False
                    break
        else:
            result.append(arr[right])
            right -= 1
            if len(result) > 1:
                if result[-1] > result[-2]:
                    print('No')
                    yes = False
                    break    
    if yes:
        print('Yes')
    
