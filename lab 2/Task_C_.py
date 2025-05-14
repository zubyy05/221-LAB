def longest_subarray_sum(n, k, arr):
    max_l = 0 
    c_sum = 0  
    s = 0  

    for i in range(n):  
        c_sum += arr[i]  
        while c_sum > k:
            c_sum -= arr[s]  
            s += 1  
        max_l = max(max_l, i - s + 1)
    return max_l  


n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(longest_subarray_sum(n, k, arr))