import sys

xa, ya, xb, yb, xc, yc = map(int, sys.stdin.readline().split())

if (xa-xb) == (xa-xc) == 0 or (ya-yb) == (ya-yc) == 0:
    print(-1.0)
elif (ya-yb) * (xa-xc) == (ya-yc) * (xa-xb):
    print(-1.0)
else:
    sab = ((xa - xb) ** 2 + (ya - yb) ** 2) ** (1 / 2)
    sac = ((xa - xc) ** 2 + (ya - yc) ** 2) ** (1 / 2)
    sbc = ((xb - xc) ** 2 + (yb - yc) ** 2) ** (1 / 2)
    sides = [sab + sac, sab + sbc, sac + sbc]
    print(2*(max(sides) - min(sides)))
