import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()
b.sort()
s = 0
for i in range(n):
    s += a[i]*b[-(i+1)]
print(s)

