import sys
from collections import deque

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
fish = []


for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            baby = [i, j]
        elif data[i][j] > 0:
            fish.append([i, j, data[i][j]])




def BC(x, y):
    res = (x >= 0 and x < n and y >= 0 and y < n)
    return res

size = 2
def search(rx, ry):

    visited = [[0] * n for _ in range(n)]
    dq = deque()
    dq.append((rx, ry))
    visited[rx][ry] = 1

    while dq:
        cx, cy = dq.popleft()
        for d in range(4):
            nx = cx+dx[d]
            ny = cy+dy[d]

            if BC(nx, ny) and not visited[nx][ny]:
                if size>=

