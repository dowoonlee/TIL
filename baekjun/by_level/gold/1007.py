import sys, math, itertools



#v_ij = <pj-pi>
#since all ele of p are used for vector
#and Nvector = Np*0.5
#so half of ele p are start point and rest of ele p are end point
def d2(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2


t = int(sys.stdin.readline())

for _ in range(t):
    tx, ty = 0, 0
    n = int(sys.stdin.readline())
    pos = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        tx += x
        ty += y
        pos.append([x, y])
    pos.sort()

    ret = sys.maxsize
    comb = list(itertools.combinations(pos, int(n/2)))
    ncomb = int(len(comb)/2)

    for element in comb[:ncomb]:
        element = list(element)
        x1t, y1t = 0, 0
        for x1, y1 in element:
            x1t += x1
            y1t += y1
        dist = (2*x1t-tx)**2 + (2*y1t-ty)**2

        ret = min(ret, math.sqrt(dist))
    print(ret)

