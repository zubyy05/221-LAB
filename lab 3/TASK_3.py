def F_M_DRIFT(x,y):
 
    mod = 107
    res = 1
 
    while y>0:
 
        if y % 2 == 1:
            res = (res*x) % mod
 
        y = y // 2
        
        x = (x*x) % mod 
 
        
    return res
 
 
x, y = map(int, input().split())
 
 
print(F_M_DRIFT(x, y))