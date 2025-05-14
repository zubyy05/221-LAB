def get_max_expression(Q, x, y):
    if y == x:
        return -1

    if y - x == 1:
        return Q[x] + Q[y] ** 2 

    mid = (x + y) // 2
    
    x_max = get_max_expression(Q, x, mid)
    y_max = get_max_expression(Q, mid + 1, y)  
    x_max_v= max(Q[x:mid+1])
    
    result = max(x_max, y_max)
    
    for j in range(mid + 1, y + 1):
        result = max(result, x_max_v+ Q[j] ** 2)
    
    return result

def solve(P, Q):
    return get_max_expression(Q, 0, P - 1)

P = int(input().strip())
Q = list(map(int, input().split()))

print(solve(P, Q))