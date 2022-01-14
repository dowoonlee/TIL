import sys

#n = int(sys.stdin.readline())
#a, b = [0]*n, [0]*n
#for i in range(n):
#    a[i], b[i] = map(int, sys.stdin.readline().split())

n=8
a, b = [1, 3, 2, 4, 6, 10, 9, 7], [8, 9, 2, 1, 4, 10, 7, 6]

maxv = max(a)
tarr = [0]*maxv
arr=[]
for i in range(n):
    tarr[a[i]-1] = b[i]
for i in range(maxv):
    if tarr[i]:
        arr.append(tarr[i])

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
print(n-max(dp))

