import sys

#n, k = map(int, sys.stdin.readline().split())

#w, v = [0]*n, [0]*n
#for i in range(n):
#    w[i], v[i] = map(int, sys.stdin.readline().split())


#n, k = 4, 7
#w, v = [6, 4, 3, 5], [13, 8, 6, 12]
n, k = 7, 19
w, v = [9, 8, 1, 6, 2, 3, 7], [89, 80, 32, 68, 74, 42, 2]
#n, k = 6, 9
#w, v = [3, 2, 4, 4, 4, 1], [6, 7, 6, 2, 10 ,5]

dp = [[0]*(k+1) for _ in range(n)]#dp[i][j] = 처음부터 i번째까지의 물건을 살펴보고, 배낭의 용량이 j였을 때 배낭에 들어간 물건의 가치합의 최댓값



for i in range(0, n):#0~i번째 물건
    for j in range(1, k+1):#용량 j
        if j<w[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])

print(dp[-1][-1])

