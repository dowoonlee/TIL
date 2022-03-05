import sys

a, b, n = map(int, sys.stdin.readline().split())

a = (a%b)*10


for i in range(n-1):
    if a>=b:
        a = (a%b)*10
    else:
        a *= 10

if a>=b:
    print(a//b)
else:
    print(0)

