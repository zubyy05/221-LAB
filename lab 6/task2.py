n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
v = [0]*(n+1)

for _ in range(m):

    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

ans = 0
for i in range(1, n+1):

    if v[i]: 
        continue
    stk = [(i, 1)]
    a = b = 0

    while stk:
        u, c = stk.pop()

        if v[u]: continue
        v[u] = c

        if c == 1: 
            a += 1
            
        else: 
            b += 1

        for j in g[u]:
            if not v[j]:

                stk.append((j, -c))

            elif v[j] == c:
                pass

    ans += max(a, b)

print(ans)
