n, r = map(int, input().split())

g = [[] for _ in range(n+1)]
s = [1] * (n+1)

for _ in range(n-1):

    u, v = map(int, input().split())

    g[u].append(v)
    g[v].append(u)

stk = [(r, 0)]
o = []

while stk:
    p, par = stk.pop()
    o.append((p, par))

    for x in g[p]:

        if x != par:
            
            stk.append((x, p))

for p, par in reversed(o):

    for x in g[p]:

        if x != par:
            s[p] += s[x]

q = int(input())

for _ in range(q):
    x = int(input())
    print(s[x])

