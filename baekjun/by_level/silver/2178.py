import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

maze = [[0]*m for _ in range(n)]
for i in range(n):
    ipt = sys.stdin.readline().rstrip()
    for j in range(m):
        maze[i][j] = int(ipt[j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if (nx >= 0 and nx < n and ny >= 0 and ny < m) and maze[nx][ny]==1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))

    return maze[n-1][m-1]

ans = bfs()
print(ans)
