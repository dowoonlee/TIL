import sys
from queue import PriorityQueue as PQ

n = int(sys.stdin.readline())

que = PQ()

for _ in range(n):
    x = int(sys.stdin.readline())
    if x!=0:
        que.put((x, x))
    else:
        if que.qsize():
            temp = que.get()
            print(temp[1])
        else:
            print(0)



