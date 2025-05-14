import sys

def binaryStringIt(s):
    left, right = 0, len(s) - 1
    position = -1

    while left <= right:
        mid = (left + right) // 2
        if s[mid] == '1':
            position = mid + 1  
            right = mid - 1  
        else:
            left = mid + 1  

    return position

t = int(input())

for k in range(t):
    s = input()
    print(binaryStringIt(s))

