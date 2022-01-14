import sys
n, x = map(int, sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
ans = ''

for i in range(n):
    if a[i]<x:
        ans+='%d '%a[i]
print(ans)