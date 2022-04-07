import sys

n = int(sys.stdin.readline())

if n<2:
    print(1)
else:
    dp = [0] * (n + 1)

    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = (2*dp[i-2]+dp[i-1])%10007

    print(dp[n])
