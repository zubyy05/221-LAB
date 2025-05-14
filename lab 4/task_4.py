n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))

d = [0] * (n + 1)

for i in range(m):

    d[u[i]] += 1
    
    d[v[i]] += 1

odd = sum(1 for x in d if x % 2 == 1)

if odd == 0 or odd == 2:
    print("YES")
else:
    print("NO")

