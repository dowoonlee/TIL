import sys

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

tree = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    tree[x][y] = 1
    tree[y][x] = 1

contg = [0]*(n+1)

def dfs(v):
    contg[v] =1
    for i in range(1, n+1):
        if tree[v][i]==1 and contg[i]==0:
            dfs(i)
dfs(1)
print(sum(contg)-1)