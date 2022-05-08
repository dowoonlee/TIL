import sys

n = int(sys.stdin.readline())
d = 10
while n>d:
    t = n%d
    if t>= d//2:
        n += d
    n -=t
    d*=10
print(n)