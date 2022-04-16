import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

ladder = [[0] * n for _ in range(2)]
snake = [[0] * m for _ in range(2)]

for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    ladder[0][i] = s
    ladder[1][i] = e
for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    snake[0][i] = s
    snake[1][i] = e


def ldr(position):
    for i in range(n):
        if position == ladder[0][i]:
            return ladder[1][i]
    return -1


def snk(position):
    for i in range(m):
        if position == snake[0][i]:
            return snake[1][i]
    return -1


visited = [0] * 101

dq = deque()
dq.append(1)
visited[1] = 1

while dq:
    node = dq.popleft()
    for dice in range(1, 7):
        nextmove = node + dice

        if nextmove > 100 or visited[nextmove]:
            continue

        is_ldr = ldr(nextmove)
        is_snk = snk(nextmove)

        if is_ldr > 0:
            nextmove = is_ldr
        if is_snk > 0:
            nextmove = is_snk

        if not visited[nextmove]:

            visited[nextmove] = visited[node] + 1
            dq.append(nextmove)

print(visited[-1]-1)
