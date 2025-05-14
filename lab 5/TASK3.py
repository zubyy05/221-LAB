from collections import deque, defaultdict

def bfs(n, m, s, d, u, v):
    graph = defaultdict(list)


    for a, b in zip(u, v):

        graph[a].append(b)
        graph[b].append(a)


    for node in graph:

        graph[node].sort()

    vis = [False] * (n + 1)
    dist = [-1] * (n + 1)
    parent = [0] * (n + 1)


    q = deque()
    q.append(s)
    vis[s] = True
    dist[s] = 0

    while q:

        curr = q.popleft()

        for neighbor in graph[curr]:
            if not vis[neighbor]:

                vis[neighbor] = True
                dist[neighbor] = dist[curr] + 1
                parent[neighbor] = curr
                q.append(neighbor)

 
    if not vis[d]:

        return -1, []


    path = []
    curr = d

    while curr:
        path.append(curr)

        curr = parent[curr]

    path.reverse()

    return dist[d], path



if __name__ == "__main__":
    n, m, s, d = map(int, input().split())
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))

    length, path = bfs(n, m, s, d, u, v)
    if length == -1:
        print(-1)
    else:
        print(length)
        print(*path)
