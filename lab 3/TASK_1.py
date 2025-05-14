def merge(a, b):
    merged = []
    i, j = 0, 0
    inv_count = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            inv_count += len(a) - i  
            j += 1

    merged.extend(a[i:])
    merged.extend(b[j:])

    return merged, inv_count


def mergeSort(arr):
    if len(arr) <= 1:
        return arr , 0
    else:
        mid = len(arr) // 2
        a1 , left_inv = mergeSort(arr[:mid])  
        a2 , right_inv = mergeSort(arr[mid:])  
        sorted , merge_inv = merge(a1, a2)

        t_inv = left_inv + right_inv + merge_inv
        return sorted , t_inv       

n = int(input())
arr = list(map(int, input().split()))
sorted_arr , inv_count = mergeSort(arr)
print(inv_count)
print(*sorted_arr)