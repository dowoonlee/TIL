import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

maxlevel = 100_000
q = deque()

cnt = [0] * (maxlevel + 1)
visited = [False] * (maxlevel + 1)
q.append(n)
cnt[n] = 1
visited[n] = True

while q:
    x = q.popleft()

    if x == k:
        print(cnt[k] - 1)
        break

    if 2 * x <= maxlevel and not visited[2 * x]:
        q.appendleft(2 * x)
        cnt[2 * x] = cnt[x]
        visited[2 * x] = True

    if x - 1 >= 0 and not visited[x - 1]:
        q.append(x - 1)
        cnt[x - 1] = cnt[x] + 1
        visited[x - 1] = True

    if x + 1 <= maxlevel and not visited[x + 1]:
        q.append(x + 1)
        cnt[x + 1] = cnt[x] + 1
        visited[x + 1] = True

