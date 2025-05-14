from collections import deque

def bfs_traversal(n, edge_list):

    graph = [[] for _ in range(n + 1)]  

    for u, v in edge_list:

        graph[u].append(v)
        graph[v].append(u)


    for adjacent in graph:

        adjacent.sort()


    vis = [False] * (n + 1)
    res = []
    queue = deque()
    queue.append(1)
    vis[1] = True

    while queue:


        c = queue.popleft()
        res.append(c)

        for adj in graph[c]:
            if not vis[adj]:
                vis[adj] = True
                queue.append(adj)

    return res


def main():
    n, m = map(int, input().split())
    edge_list = []

    for _ in range(m):
        u, v = map(int, input().split())
        edge_list.append((u, v))

    res = bfs_traversal(n, edge_list)
    print(' '.join(str(node) for node in res))


if __name__ == "__main__":
    main()




