import sys

n = int(sys.stdin.readline())

for i in range(n, 0, -1):
    s = " " * (n - i) + "*" * i
    print(s)
