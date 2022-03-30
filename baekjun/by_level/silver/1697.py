import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

maxlevel = 100000

cnt = [0]*(maxlevel + 1)

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(cnt[x])
            break
        for j in (x-1,x+1,x*2):
            if 0<= j <= maxlevel and not cnt[j]:
                cnt[j] = cnt[x] +1
                q.append(j)
bfs()