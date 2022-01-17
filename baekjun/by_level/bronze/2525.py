import sys

h, m = map(int, sys.stdin.readline().split())
p = int(sys.stdin.readline())

t = h*60+m+p

h , m = t//60, t%60
h-=24*(h//24)

print(h, m)


