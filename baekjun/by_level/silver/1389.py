import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1


def bfs(root):
    distance = [-1]*(n+1)
    distance[root] = 0
    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        for next_node in range(1, n+1):
            if graph[node][next_node] and distance[next_node]<0:
                q.append(next_node)
                distance[next_node] = distance[node]+1
    distance[0] = 0
    return sum(distance)


dist = [0]*n


for i in range(n):
    dist[i] = bfs(i+1)
print(dist.index(min(dist))+1)