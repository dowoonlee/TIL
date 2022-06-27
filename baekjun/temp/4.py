import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
shop = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
mannq = []
for i in range(n):
    for j in range(m):
        if shop[i][j] == 4:
            siru = (i, j)
        elif shop[i][j] == 3:
            mannq.append((i, j))


def bc(x, y):
    return x < 0 or x >= n or y < 0 or y >= m


for mq in mannq:
    for i in range(-k, k + 1):
        for j in range(-k, k + 1):
            mqx, mqy = mq[0] + i, mq[1] + j
            if bc(mqx, mqy):
                continue

            if abs(i) + abs(j) <= k and shop[mqx][mqy] != 4:
                shop[mqx][mqy] = 3


def search(root):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    shop[root[0]][root[1]] = -1

    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        x, y = node[0], node[1]

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if bc(nx, ny) or shop[nx][ny] == 3 or shop[nx][ny]<0:
                continue
            if shop[nx][ny] == 2:
                return -shop[x][y]
            shop[nx][ny] = shop[x][y] - 1
            q.append((nx, ny))
    return -1


print(search(siru))
