def bubbleSort(arr, n):                                                    
    for i in range(n-1):
        idx = False
        for j in range(n-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                idx = True
 
        if not idx:
            break
    for z in range(len(arr)):
        print(arr[z], end=' ')
 
n = int(input())
idx = list(map(int, input().split()))
 
bubbleSort(idx, n)