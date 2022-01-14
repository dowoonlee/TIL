import sys


def dist(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2

t = int(sys.stdin.readline())


for _ in range(t):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    planet = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    ans = 0
    for xxc in planet:
        d1, d2 = dist(x1, y1, xxc[0], xxc[1]), dist(x2, y2, xxc[0], xxc[1])
        r2 = xxc[2]**2
        if (d1-r2)*(d2-r2)>0:
            pass
        else:
            ans+=1

    print(ans)

