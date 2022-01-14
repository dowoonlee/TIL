import sys

#n = int(sys.stdin.readline())
#ns = list(map(int, sys.stdin.readline().split()))

n, ns = 10, [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
#n, ns = 10, [2, 1, -4, 3, 4, -4, 6, 5, -5, 1]

dp = [0] * n
dp[0] = ns[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]+ns[i], ns[i])
print(dp)


