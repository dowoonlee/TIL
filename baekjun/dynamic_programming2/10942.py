import sys
read = sys.stdin.readline

#n = int(read())
#ns = list(map(int, read().split()))
#m = int(read())

n = 7
ns = [1, 2, 1, 3, 1, 2, 1]
m = 4

dp = [[0]*n for _ in range(n)]


for i in range(n):
    dp[i][i]=1

for i in range(n-1):
    if ns[i]==ns[i+1]:
        dp[i][i+1]=1

for l in range(2, n):
    for i in range(n-l):
        if ns[i] == ns[i+l] and dp[i+1][i+l-1]==1:
            dp[i][i+l]=1


for _ in range(m):
    s, e = map(int, read().split())
    print(dp[s-1][e-1])




