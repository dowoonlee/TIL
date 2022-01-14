import sys

N, M = map(int, sys.stdin.readline().split())
hs = list(map(int,sys.stdin.readline().split()))

#case1
#N, M = 4, 7
#hs = [20, 15, 10, 17]
#case2
#N, M = 5, 20
#hs = [4, 42, 40, 26, 46]


low, high = 0, max(hs)

while low <= high:
    mid = (low + high) // 2
    get_tree = sum([i - mid if i > mid else 0 for i in hs])

    if get_tree < M: # (left, mid-1) / mid is bigger than answer
        high = mid-1

    else:# (mid+1, right)
        low = mid+1
        ans = mid

print(ans)