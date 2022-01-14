import sys

n, k = map(int, sys.stdin.readline().split())
if n-k<k:
    k = n-k

ans = 1

for i in range(k):
    ans *= (n-i)
    ans /= (i+1)

print(int(ans))
