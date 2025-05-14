from collections import deque

n, m = map(int, input().split())
z = [[] for _ in range(n+1)]
c = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())

    z[a].append(b)
    c[b] += 1

q = deque()

for i in range(1, n+1):

    if c[i] == 0:
        q.append(i)

r = []
while q:

    x = q.popleft()
    r.append(x)

    for y in z[x]:
        c[y] -= 1
        
        if c[y] == 0:
            q.append(y)

print(*r if len(r) == n else [-1])

