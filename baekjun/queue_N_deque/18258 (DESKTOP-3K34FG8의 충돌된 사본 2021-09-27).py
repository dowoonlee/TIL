import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

for i in range(n):
    cmd = list(map(str, sys.stdin.readline().split()))
    if cmd[0] == 'push':
        q.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if len(q):
            temp = q.popleft()
            print(temp)
            q.appendleft(temp)
        else:
            print(-1)
    else:
        if len(q):
            temp = q.pop()
            print(temp)
            q.append(temp)
        else:
            print(-1)
