def two_sum_trouble(n, s, arr):
    left = 0
    right = n - 1  
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == s:
            print(left + 1, right + 1)  
            return
        elif current_sum < s:
            left += 1
        else:
            right -= 1
    
    print(-1)  


n, s = map(int, input().split())
arr = list(map(int, input().split()))
two_sum_trouble(n, s, arr)