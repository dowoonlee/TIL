import sys


n, m = map(int, sys.stdin.readline().split())
tree = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    tree[u][v] = 1
    tree[v][u] = 1

visited = [0]*(n+1)
visited[0] = 1

def dfs(x):
    visited[x] = 1
    for i in range(1, n+1):
        if tree[x][i]==1 and not visited[i]:
            dfs(i)


cnt = 0
for j in range(1, n+1):
    if not visited[j]:
        print(visited)
        dfs(j)
        cnt+=1
print(visited)
print(cnt)
