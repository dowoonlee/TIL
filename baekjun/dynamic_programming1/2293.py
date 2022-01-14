import sys

#n, k = map(int, sys.stdin.readline().split())
#coins = [int(sys.stdin.readline()) for _ in range(n)]

n, k = 3, 10
coins = [1, 2, 5]

dp = [0] * (k+1)
dp[0] = 1

for c in coins:
    for j in range(1, k+1):
        if j-c >= 0:
            dp[j] += dp[j-c]
print(dp)





