import sys

x, y = map(int, sys.stdin.readline().split())

init_z = int(100*y/x)

if init_z>=99:
    print(-1)
else:
    k_min = ((1+init_z)*x - 100*y)/(99-init_z)
    ans = int(k_min) + bool(k_min%1)
    print(ans)