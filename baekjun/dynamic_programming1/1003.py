import sys

t = int(sys.stdin.readline())

check = [0]*41
dp = [[0]*2 for _ in range(41)]#dp[for n ][0 /1]
dp[0][0], check[0] = 1, 1
dp[1][1], check[1] = 1, 1
dp[2][0], dp[2][1], check[2] = 1, 1, 1

for i in range(3, 41):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

for _ in range(t):
    n = int(sys.stdin.readline())
    print('%d %d'%(dp[n][0], dp[n][1]))

