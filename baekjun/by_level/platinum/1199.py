import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def chk(g):
    for i in range(len(g)):
        s = sum(g[i])
        if s % 2:
            return False
    return True


def dfs(now):
    for i in range(n):
        if graph[now][i]:
            graph[now][i] -= 1
            graph[i][now] -= 1
            dfs(i)
    print(now + 1, end=" ")


if chk(graph):
    dfs(0)
else:
    print(-1)
