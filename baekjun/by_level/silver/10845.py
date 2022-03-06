import sys

n = int(sys.stdin.readline())

q = []
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        q.append(int(order[1]))
    elif order[0] == "pop":
        if q:
            print(q.pop(0))
        else:
            print(-1)
    elif order[0] == "size":
        print(len(q))
    elif order[0] == "empty":
        print(1-int(bool(q)))
    elif order[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)
