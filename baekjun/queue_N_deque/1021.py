import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))

dq = deque([i+1 for i in range(n)])
nr = 0
for i in data:
    pos = dq.index(i)
    if pos<0.5*len(dq):
        dq.rotate(-pos)
        nr += pos

    else:
        dq.rotate(len(dq)-pos)
        nr += (len(dq)-pos)
    dq.popleft()

print(nr)