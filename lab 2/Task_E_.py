import sys

def lower_bound(arr, x):

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left+ right) // 2

        if arr[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    return left

def upper_bound(arr, y):

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= y:
            left = mid + 1

        else:
            right = mid - 1

    return left

p, q = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

output = []
for _ in range(q):
    
    x, y = map(int, sys.stdin.readline().split())
    lower = lower_bound(arr, x)
    upper = upper_bound(arr, y)
    output.append(str(upper - lower))

sys.stdout.write("\n".join(output) + "\n")



