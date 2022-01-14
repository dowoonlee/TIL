import sys

a, b = map(str, sys.stdin.readline().split())
ans = int(a, 2)+int(b, 2)
print(format(ans ,"b"))
