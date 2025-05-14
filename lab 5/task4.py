from collections import deque, defaultdict

def bfs(start, graph, N):

    dist = [-1] * (N + 1)
    prev = [None] * (N + 1)
    queue = deque([start])
    dist[start] = 0

    while queue:
        
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                prev[v] = u
                queue.append(v)
    
    return dist, prev

def reconstruct_path(prev, end):

    path = []

    while end is not None:
        path.append(end)
        end = prev[end]

    return path[::-1]

def main():

    N, M, S, D, K = map(int, input().split())
    
    graph = defaultdict(list)

    for _ in range(M):

        u, v = map(int, input().split())
        graph[u].append(v)

    if S == K:
        dist_K, prev_K = bfs(K, graph, N)
        if dist_K[D] == -1:
            print(-1)
            return
        
        path = reconstruct_path(prev_K, D)
        print(len(path) - 1)
        print(" ".join(map(str, path)))

    else:
        dist_S, prev_S = bfs(S, graph, N)
        dist_K, prev_K = bfs(K, graph, N)

        if dist_S[K] == -1 or dist_K[D] == -1:

            print(-1)
            return

        path1 = reconstruct_path(prev_S, K)
        path2 = reconstruct_path(prev_K, D)[1:]  

        final_path = path1 + path2

        print(len(final_path) - 1)

        print(" ".join(map(str, final_path)))

if __name__ == "__main__":
    main()


