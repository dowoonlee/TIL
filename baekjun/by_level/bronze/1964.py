import sys

n = int(sys.stdin.readline())

dp = [0]*(n+1)

dp[0] = 1
dp[1] = 4 + dp[0]

for i in range(2, n+1):
    dp[i] = (3*i+1 + dp[i-1])%45678
print(dp[n])
