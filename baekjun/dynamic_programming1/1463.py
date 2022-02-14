import sys

n = int(sys.stdin.readline())

dp = [0]*(n+1)
if n<4:
    if n==1:
        print(0)
    else:
        print(1)
else:
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    for i in range(5, n+1):
        tdp = []
        if i%3==0:
            tdp.append(dp[int(i/3)]+1)
            print(dp[int(i/3)]+1)
        if i%2==0:
            tdp.append(dp[int(i/2)]+1)
            print(dp[int(i/2)]+1)
        tdp.append(dp[i-1]+1)
        print(dp[i-1]+1)
        dp[i] = min(tdp)

    print(dp)
    print(dp[n])

