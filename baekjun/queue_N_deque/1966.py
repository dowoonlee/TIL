import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    n, m =  map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))
    dq = deque(data)
    np = 0
    while True:
        if (dq[0] == max(dq)) and m==0:
            dq.popleft()
            np+=1
            break

        elif dq[0] == max(dq):
            dq.popleft()
            np+=1
            m-=1
        else:
            dq.rotate(-1)
            m-=1

        if m<0:
            m += len(dq)

    print(np)