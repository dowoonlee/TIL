import sys

x, y = map(int, sys.stdin.readline().split())


x4 = (x-1)//4
xr = (x-1)%4

y4 = (y-1)//4
yr = (y-1)%4

dx = abs(x4-y4) + abs(xr-yr)
print(dx)