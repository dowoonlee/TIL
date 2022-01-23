import sys

m = int(sys.stdin.readline())
cup = [1, 2, 3]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    if x==y:
        pass
    else:
        xidx, yidx = cup.index(x), cup.index(y)
        cup[xidx], cup[yidx] = y, x
print(cup[0])