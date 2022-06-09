import sys

n = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

p = [i for i in range(n)]


def is_crossed(i, j):
    l1 = lines[i]
    l2 = lines[j]

    slope1 = slope(l1)
    slope2 = slope(l2)

    if slope1 == slope2 and slope1 != float("inf"):
        intercept1 = l1[1] - slope1 * l1[0]
        intercept2 = l2[1] - slope2 * l2[0]
        if intercept1 == intercept2:
            


        else:
            return False
    elif slope1 == slope2:
        if l1[0] == l2[0]:
            xx, yy = intersect_point(slope1, slope2, l1[1] - slope1 * l1[0], l1[1] - slope1 * l1[0])
            (xx>l1[0])*()
        else:
            return False
    else:
        xx, yy = intersect_point(slope1, slope2, l1[1] - slope1 * l1[0], l1[1] - slope1 * l1[0])


def slope(line):
    x1, y1, x2, y2 = line[0], line[1], line[2], line[3]
    if x1 == x2:
        return float("inf")
    else:
        return (y2 - y1) / (x2 - x1)


def intersect_point(sl1, sl2, inter1, inter2):
    x = (inter2 - inter1) / (sl1 - sl2)
    y = sl1*x+inter1
    return x, y
