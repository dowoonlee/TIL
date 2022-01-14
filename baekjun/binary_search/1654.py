import sys


k, n = map(int, sys.stdin.readline().split())
ks = list(map(int, sys.stdin.readlines()))

h, l = 1, sum(ks)//n

while l <= h:
    mid = (l + h) // 2
    n_mid = sum([i // mid for i in ks])

    if n_mid < n: # (left, mid-1) / mid is bigger than answer
        h = mid-1

    else:# (mid+1, right)
        l = mid+1
        ans = mid

print(ans)
