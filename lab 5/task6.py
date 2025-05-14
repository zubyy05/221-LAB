from collections import deque

r, c = map(int, input().split())
g = [list(input().strip()) for _ in range(r)]
v = [[0]*c for _ in range(r)]
d = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    v[x][y] = 1
    cnt = 1 if g[x][y] == 'D' else 0

    while q:
        i, j = q.popleft()

        for dx, dy in d:

            ni, nj = i + dx, j + dy

            if 0 <= ni < r and 0 <= nj < c and not v[ni][nj] and g[ni][nj] != '#':

                v[ni][nj] = 1
                if g[ni][nj] == 'D':
                    cnt += 1

                q.append((ni, nj))
    return cnt

ans = 0

for i in range(r):
    for j in range(c):
        if not v[i][j] and g[i][j] != '#':
            ans = max(ans, bfs(i, j))

print(ans)
