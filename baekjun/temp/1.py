import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
ab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for a, b in ab:
    x -= a*b
if x:
    print("No")
else:
    print("Yes")