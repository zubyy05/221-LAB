n, m = map(int, input().split())
matrix = [[0] * n for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())
    matrix[u - 1][v - 1] = w

for row in matrix:
    print(' '.join(map(str, row)))

