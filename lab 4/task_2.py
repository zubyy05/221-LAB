n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))


adjacency_list = [[] for _ in range(n + 1)]


for i in range(m):
    adjacency_list[u[i]].append((v[i], w[i]))


for node in range(1, n + 1):
    c = adjacency_list[node]
    if c:
        f_e = ' '.join(f'({v},{w})' for v, w in c)
        print(f"{node}: {f_e}")
    else:
        print(f"{node}:")
