import sys
from collections import deque

n = int(sys.stdin.readline())

rgb = {"R": 1, "G": 2, "B": 3}

fig = [[0] * n for _ in range(n)]
for i in range(n):
    c = sys.stdin.readline().rstrip()
    for j in range(n):
        fig[i][j] = rgb[c[j]]


def bc(x, y):
    return (x >= 0 and x < n and y >= 0 and y < n)


visited = [[0] * n for _ in range(n)]


def search1(root, color, cnt):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    dq = deque()
    dq.append(root)

    while dq:
        node = dq.pop()
        visited[node[0]][node[1]] = cnt
        for d in range(4):
            nx = node[0] + dx[d]
            ny = node[1] + dy[d]
            if bc(nx, ny) and fig[nx][ny] == color and not visited[nx][ny]:
                dq.append([nx, ny])
    return


cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt += 1
            search1([i, j], fig[i][j], cnt)
print(cnt, end=" ")

for i in range(n):
    for j in range(n):
        if fig[i][j] == 1:
            fig[i][j] = 2

visited = [[0] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt += 1
            search1([i, j], fig[i][j], cnt)

print(cnt)
