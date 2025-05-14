N = int(input())
id = list(map(int, input().split(" ")))
marks = list(map(int, input().split(" ")))
 
student = list(zip(id, marks))
 
 
def sortingAgain(arr, n):
 
    sort = 0
 
    for i in range(n):
        idx = i
 
        for j in range(i+1, n):
            
            if (arr[j][1] > arr[idx][1]) or (arr[j][1] == arr[idx][1] and arr[j][0] < arr[idx][0]):
                
                idx = j
                
                
        if idx != i:
 
            arr[i], arr[idx] = arr[idx], arr[i]
 
            sort += 1
        
    return sort
    
 
s = sortingAgain(student, N)
print(f"Minimum swaps: {s}")
 
for k in student:
    print(f"ID: {k[0]} Mark: {k[1]}")