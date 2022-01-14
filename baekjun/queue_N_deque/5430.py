import sys
from collections import deque
import time

t0 = time.time()
t = int(sys.stdin.readline())

def AC(p, deq):
    j = 0
    F = True
    R = 1#left
    while j < len(p) and F:
        if p[j]=='R':
            R *= (-1)
        elif p[j] == 'D':
            try:
                if R+1:#R=1, left
                    deq.popleft()
                else:#R=-1, right
                    deq.pop()
            except IndexError:
                F = False
        j+=1
    if F and deq:
        if R+1:
            return list(deq)
        else:
            deq.reverse()
            return list(deq)
    else:
        return 'error'



for i in range(t):
    p = list(map(str,sys.stdin.readline().rstrip()))
    n = int(sys.stdin.readline())
    tdata = sys.stdin.readline().rstrip()[1:-1].split(",")
    if n==0:
        print('error')
        break
    else:
        data = []
        for i in range(n):
            data.append(int(tdata[i]))
    dq = deque(data)
    ans = AC(p, dq)

    if ans!='error':
        print('[', end="")
        for j in ans[0:-1]:
            print('%d'%j, end=",")
        print('%d'%ans[-1], end="")
        print(']')

    else:
        print(ans)
