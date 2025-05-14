import sys
 
def exp(a, b, mod):
    res = 1
    a = a % mod
    
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % mod
        a = (a * a) % mod
        b = b // 2
 
    return res
 
def sum(a, n, m):
    if a == 1:
        return n % m
    
    k = m * (a - 1)
    a_n_mod_k = exp(a, n, k)
    S = (a * (a_n_mod_k - 1)) // (a - 1)
 
    return S % m
 
 
data = sys.stdin.read().split()
T = int(data[0])
index = 1
new_res = []
 
for _ in range(T):
    a = int(data[index])
    n = int(data[index+1])
    m = int(data[index+2])
    index += 3
    new_res.append(str(sum(a, n, m)))
 
 
print('\n'.join(new_res))