import sys

l = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())

x = max(a//c+bool(a%c), b//d+bool(b%d))
print(l-x)