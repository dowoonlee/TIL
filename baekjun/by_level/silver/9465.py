import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    stickers = []
    for ti in range(2):
        stickers.append(list(map(int ,sys.stdin.readline().split())))
    dp = [[0]*n for _ in range(2)]
    dp[0][0], dp[1][0] = stickers[0][0], stickers[1][0]

    for i in range(1, n):
        dp[0][i] = max(dp[1][i - 1] + stickers[0][i], dp[0][i - 1])
        dp[1][i] = max(dp[0][i - 1] + stickers[1][i], dp[1][i - 1])
    max1, max2 = max(dp[0]), max(dp[1])
    print(max(max1,max2))



