import sys
#n = int(sys.stdin.readline())
#a = list(map(int, sys.stdin.readline().split()))
a = [1, 5, 2, 1, 4, 3, 4, 5, 2, 1]
n = len(a)

def lis(arr):
    dp = [0] * n
    dp[0] = 1
    maxv = 1
    for i in range(n):
        dp[i]=1
        for j in range(i):
            if arr[j]<arr[i] and dp[j]+1>dp[i]:
                dp[i] = dp[j] + 1
                if maxv < dp[i]:
                    maxv = dp[i]
    return dp

inc, dec = lis(a), lis(a[::-1])
dec = dec[::-1]
dp = [0]*n
for i in range(n):
     dp[i] = inc[i]+dec[i]-1
print(max(dp))