import math
import sys
input = sys.stdin.read

data = input().split()
idx = 0

x = int(data[idx])
idx += 1

y = int(data[idx])
idx += 1


adj = [[] for _ in range(x + 1)]  

for i in range(1, x + 1):

    for j in range(1, x + 1):

        if i != j and math.gcd(i, j) == 1:
            adj[i].append(j)
    adj[i].sort()


res = []
for _ in range(y):

    X = int(data[idx])
    idx += 1

    K = int(data[idx])
    idx += 1

    if K <= len(adj[X]):
        res.append(str(adj[X][K - 1]))

    else:
        res.append("-1")

print("\n".join(res))
