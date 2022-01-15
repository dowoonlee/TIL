import sys
from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def DFS(graph, x, y):
    stack = deque()
    stack.append((x, y))
    graph[x][y]=0

    while stack:
        curx, cury = stack.popleft()
        for i in range(4):#EWSN
            nx, ny = curx+dx[i], cury+dy[i]
            if nx<0 or ny<0 or nx>=len(graph) or ny>=len(graph[0]):#B.C
                continue
            if graph[nx][ny]:
                graph[nx][ny] = 0 #visited
                stack.append((nx, ny))
    return


t = int(sys.stdin.readline())

for _ in range(t):
    nworm = 0
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0]*n for _ in range(m)]
    for i in range(k):
        x, y = map(int,sys.stdin.readline().split())
        graph[x][y] = 1

    for x in range(m):
        for y in range(n):
            if graph[x][y]:
                DFS(graph, x, y)
                nworm+=1
    print(nworm)


