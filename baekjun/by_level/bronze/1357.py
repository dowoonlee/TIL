import sys

x, y = map(str, sys.stdin.readline().split())
ans = int(str(int(x[::-1])+int(y[::-1]))[::-1])
print(ans)