def balanced_bst(arr):
    if not arr:
        return []
    mid = len(arr) // 2

    root = arr[mid]

    left = balanced_bst(arr[:mid])

    right = balanced_bst(arr[mid+1:])
    
    return [root] + left + right



N = int(input())
A = list(map(int, input().split()))


order = balanced_bst(A)

print(' '.join(map(str, order)))