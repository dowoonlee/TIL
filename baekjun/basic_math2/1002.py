import sys
t = int(sys.stdin.readline())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    a, b, c = 2*(x2-x1), 2*(y2-y1), (r1**2-r2**2)-(x1**2-x2**2)-(y1**2-y2**2)

    if a==0 and b==0:
        if c==0:
            print(-1)
        else:
            print(0)
    elif a==0 and b!=0:
        d = abs(y1-c/b)
        if d<r1:
            print(2)
        elif d==r1:
            print(1)
        else:
            print(0)
    elif a!=0 and b==0:
        d = abs(x1-c/a)
        if d<r1:
            print(2)
        elif d==r1:
            print(1)
        else:
            print(0)
    else:
        d = abs(a*x1+b*y1-c)/((a**2+b**2)**(0.5))
        if d<r1:
            print(2)
        elif d==r1:
            print(1)
        else:
            print(0)
