import sys

t = int(sys.stdin.readline())


def dpcal(arr):
    n = len(arr)
    cs = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        cs[i] = cs[i-1]+arr[i-1]
    dp = [[0] * n for _ in range(n)]
    for i in range(1, n):  # 1~n-1 for length
        for j in range(0, n-i):
            dp[j][j+i] = (cs[j+i+1] - cs[j]) + min([dp[j][j+k] + dp[j+k+1][j+i] for k in range(i)])


    return dp[0][-1]

for _ in range(t):
    k = int(sys.stdin.readline())
    ks = list(map(int, sys.stdin.readline().split()))
    print(dpcal(ks))






