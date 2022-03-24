import sys

k, n = map(int, sys.stdin.readline().split())
ks = [int(sys.stdin.readline()) for _ in range(k)]
left, right = 1, sum(ks)//n
while left<=right:
    mid = (left + right) // 2
    n_mid = sum([i // mid for i in ks])
    print(left, n_mid, right)
    if n_mid < n: # (left, mid-1) / mid is bigger than answer
        right = mid-1
    elif n_mid>=n:# (mid+1, right)
        left = mid+1
        ans = mid

print(ans)