def f(n, e):
    
    from collections import defaultdict
    g = defaultdict(list)
    for u, v in e:
        g[u].append(v)

    v = [0] * (n + 1)

    for i in range(1, n + 1):

        if v[i] == 0:
            s = [(i, 0)]
            p = []

            while s:
                x, idx = s.pop()

                if v[x] == 0:
                    v[x] = 1
                    s.append((x, 1))

                    for y in g[x]:

                        if v[y] == 0:

                            s.append((y, 0))

                        elif v[y] == 1:
                            return "YES"
                        
                elif idx == 1:
                    v[x] = 2
    return "NO"

if __name__ == "__main__":
    n, m = map(int, input().split())
    e = [tuple(map(int, input().split())) for _ in range(m)]
    print(f(n, e))
