import sys

n = int(sys.stdin.readline())

dp = [0]*(n+1)
dp[1] = 1

for i in range(2, n + 1):
    minV = sys.maxsize
    j = 1

    while (j ** 2) <= i:
        minV = min(minV, dp[i - (j ** 2)])
        j += 1
    dp[i] = minV+1
print(dp[n])
