import sys

n, m = map(int, sys.stdin.readline().split())

tab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

st = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        st[i + 1][j + 1] = st[i][j + 1] + st[i + 1][j] - st[i][j] + tab[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(st[x2][y2] - st[x1-1][y2] -st[x2][y1-1] + st[x1-1][y1-1])
