import sys
from collections import deque


m, n = map(int, sys.stdin.readline().split())

tmt = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

q = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


for i in range(n):
    for j in range(m):
        if tmt[i][j]==1:
            q.append([i, j])

def bfs():
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]

            if (nx>=0 and nx<n) and (ny>=0 and ny<m) and tmt[nx][ny]==0:
                tmt[nx][ny] = tmt[x][y] + 1
                q.append([nx, ny])
bfs()

res = 0
for i in tmt:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res-1)
