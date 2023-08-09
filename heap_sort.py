class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[largest] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr, n, largest)
        # code here
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(n // 2, -1, -1):
            self.heapify(arr, n, i)
        # code here
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)

arr = [1, 12, 9, 5, 6, 10]
h = Solution()
n = len(arr)
h.HeapSort(arr, n)
print("Sorted array is")
for i in range(n):
      print("%d " % arr[i], end='')
  
