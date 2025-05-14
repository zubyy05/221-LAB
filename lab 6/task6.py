from collections import defaultdict, deque

n = int(input())
w = [input() for _ in range(n)]

g = defaultdict(list)
d = [0]*26
a = set()

for x in w:
    for c in x:
        a.add(ord(c)-97)

ok = True
for i in range(n-1):
    s, t = w[i], w[i+1]
    f = False

    for j in range(min(len(s), len(t))):
        if s[j] != t[j]:

            u, v = ord(s[j])-97, ord(t[j])-97
            g[u].append(v)
            d[v] += 1
            f = True
            break

    if not f and len(s) > len(t):
        ok = False
        break

if not ok:
    print(-1)

else:
    q = [i for i in range(26) if d[i] == 0 and i in a]
    q.sort()
    res = ''

    while q:
        u = q.pop(0)
        res += chr(u+97)
        tmp = []

        for v in g[u]:
            d[v] -= 1
            if d[v] == 0:
                tmp.append(v)

        q += tmp
        q.sort()

    if len(res) != len(a):
        print(-1)
        
    else:
        print(res)
