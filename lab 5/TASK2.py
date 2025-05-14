n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))

g = [[] for _ in range(n + 1)]
for i in range(m):

    g[u[i]].append(v[i])
    g[v[i]].append(u[i])

for adj in g:
    adj.sort(reverse=True)

vis = [0] * (n + 1)
stk = [1]
res = []

while stk:
    x = stk.pop()

    if not vis[x]:
        vis[x] = 1
        res.append(x)

        for y in g[x]:

            if not vis[y]:
                stk.append(y)

print(' '.join(map(str, res)))
