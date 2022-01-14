import sys

#n = int(sys.stdin.readline())
#w = [int(sys.stdin.readline()) for _ in range(n)]

w = [6, 10, 13, 9]#, 8, 1]
n = len(w)

dp = [0]*n

if n<3:
    print(sum(w))

else:
    dp[0] = w[0]
    dp[1] = w[0] + w[1]
    dp[2] = max([w[0]+w[1], w[0]+w[2], w[1]+w[2]])

    for i in range(3, n):
        dp[i] = max([dp[i-3] + w[i-1] + w[i], dp[i-2] + w[i], dp[i-1]])

    print(max(dp))