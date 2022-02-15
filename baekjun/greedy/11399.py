import sys

#n = int(sys.stdin.readline())
#p = list(map(int, sys.stdin.readline().split()))
n, p = 5, [3, 1, 4, 3, 2]
p.sort()

ans = [0]*n
ans[0] = p[0]

for i in range(1, n):
    ans[i] = ans[i-1]+p[i]
print(ans)
print(sum(ans))
