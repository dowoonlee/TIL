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
            fish.append((i, j))
nfish = len(fish)

data[baby[0]][baby[1]] = 0


def BC(x, y):
    res = (x >= 0 and x < n and y >= 0 and y < n)
    return res


size = 2


def search(rx, ry):
    visited = [[0] * n for _ in range(n)]
    dq = deque()
    dq.append((rx, ry, 0))
    visited[rx][ry] = 1
    dist_list = []
    min_dist = sys.maxsize
    while dq:
        cx, cy, dist = dq.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            if BC(nx, ny) and not visited[nx][ny]:
                if size >= data[nx][ny]:
                    visited[nx][ny] = 1
                    if data[nx][ny] > 0 and data[nx][ny] < size:
                        min_dist = dist
                        dist_list.append((nx, ny, dist + 1))
                    if dist + 1 <= min_dist:
                        dq.append((nx, ny, dist + 1))
    if dist_list:
        dist_list.sort()
        return dist_list[0]
    else:
        return False


ans = 0
neat = 0
while nfish:
    res = search(baby[0], baby[1])
    if not res:
        break
    baby[0] = res[0]
    baby[1] = res[1]
    ans += res[2]
    neat += 1
    nfish -= 1
    if size == neat:
        size += 1
        neat = 0
    data[baby[0]][baby[1]] = 0
print(ans)
