import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

dq = deque([i+1 for i in range(n)])
ans = []

while dq:
    dq.rotate(-(k-1))
    ans.append(dq.popleft())

print("<", end='')
for i in ans[0: -1]:
    print("%d"%i, end=", ")

print("%d>"%ans[-1], end='')



