import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[0] * m for _ in range(n)]
for i in range(n):
    ipt = sys.stdin.readline().rstrip()
    for j in range(m):
        graph[i][j] = int(ipt[j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1


def bc(x, y):
    return x < 0 or x >= n or y < 0 or y >= m


def search(rx, ry, can_break):
    dq = deque()
    dq.append((rx, ry, can_break))

    while dq:
        x, y, able = dq.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][able]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if bc(nx, ny):
                continue
            if graph[nx][ny] == 1 and not able:
                visited[nx][ny][1] = visited[x][y][0] + 1
                dq.append((nx, ny, 1))
            elif graph[nx][ny] == 0 and not visited[nx][ny][able]:
                visited[nx][ny][able] = visited[x][y][able] + 1
                dq.append((nx, ny, able))
    return -1


print(search(0, 0, 0))
