import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

tree = [[100_001] * n for _ in range(n)]

for i in range(n):
    tree[i][i] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if tree[a - 1][b - 1] > c:
        tree[a - 1][b - 1] = c

for node in range(n):
    for i in range(n):
        for j in range(n):
            tree[i][j] = min(tree[i][node] + tree[node][j], tree[i][j])

for i in range(n):
    for j in range(n):
        print(tree[i][j], end=" ")
    print()
