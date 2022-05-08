import sys

v, e = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(e)]

edges = sorted(edges, key=lambda x: x[2])
p = [i for i in range(v + 1)]


def findset(x):
    if x == p[x]:
        return x
    else:
        p[x] = findset(p[x])
        return p[x]


def union(x, y):
    p[findset(y)] = findset(x)
    return


cost = 0
for v1, v2, w in edges:
    if findset(v1) != findset(v2):
        union(v1, v2)
        cost += w
print(cost)
