import sys

t = 0
for _ in range(4):
    t+=int(sys.stdin.readline())
print(t//60)
print(t%60)