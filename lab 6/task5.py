from collections import deque

n = int(input())
g = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

def bfs(s):

    d = [-1] * (n+1)
    d[s] = 0
    q = deque([s])

    while q:
        x = q.popleft()

        for y in g[x]:

            if d[y] == -1:
                d[y] = d[x] + 1
                q.append(y)
    m = max(d)

    i = d.index(m)

    return i, m

a, k = bfs(1)

b, dist = bfs(a)

print(dist)
print(a, b)
