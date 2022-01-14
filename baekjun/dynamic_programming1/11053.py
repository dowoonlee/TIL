import sys

#n = int(sys.stdin.readline())
#a = list(map(int, sys.stdin.readline().split()))

a = [10, 20, 10, 30, 20, 50]
n = len(a)

dp = [0] * n
dp[0] = 1
maxv = 1
for i in range(n):
    dp[i]=1
    for j in range(i):
        if a[j]<a[i] and dp[j]+1>dp[i]:
            dp[i] = dp[j] + 1
            if maxv < dp[i]:
                maxv = dp[i]
print(dp)


