def binarysearch(arr, n, k):
    left = 0
    right = len(arr) - 1
    mid = 0
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == k:
            return mid
        if arr[mid] < k:
            left = mid + 1
        if arr[mid] < k:
            right = mid - 1
	            
    return -1



print(binarysearch([1, 2, 3, 4, 5], 5, 3))
