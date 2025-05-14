n = int(input())


adj_matrix = [[0] * n for _ in range(n)]

for i in range(n):

    split = list(map(int, input().split()))
    k = split[0]       
    l = split[1:]      

    for j in l:
        adj_matrix[i][j] = 1


for row in adj_matrix:
    print(' '.join(map(str, row)))
