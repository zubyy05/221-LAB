from collections import deque

def f():
    n = int(input())

    a, b, x, y = map(int, input().split())
    q = deque([(a, b, 0)])
    v = {(a, b)}

    m = [(2,1),(1,2),(-1,2),
         (-2,1),     (-2,-1),
         (-1,-2),(1,-2),(2,-1)]

    while q:

        p, q1, z = q.popleft()
        if (p, q1) == (x, y):
            print(z)
            return

        for dx, dy in m:
            i, j = p + dx, q1 + dy

            if 1 <= i <= n and 1 <= j <= n and (i, j) not in v:

                v.add((i, j))

                q.append((i, j, z+1))
                
    print(-1)

f()


