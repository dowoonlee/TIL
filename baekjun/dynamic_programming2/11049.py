import sys

#n = int(sys.stdin.readline())
#r, c = [0]*n, [0]*n
#for i in range(n):
#    r[i], c[i] = map(int, sys.stdin.readline().split())
r = [5, 3, 2]
c = [3, 2, 6]

rc = r
rc.append(c[-1])


def dpcal(rc):
    n = len(rc)-1
    dp = [[0] * n for _ in range(n)]

    for i in range(1, n):  # 1~n-1 for length
        for j in range(0, n-i):
            print(j, j+i)
            for k in range(i):
                print(j, j+k, '/', j+k+1, j+i, '/', '(%d,%d,%d)'%(j,j+k+1 ,j+i+1))
            dp[j][j+i] = min([dp[j][j+k] + dp[j+k+1][j+i] + rc[j]*rc[j+k+1]*rc[j+i+1] for k in range(i)])

    return dp[0][-1]


x = dpcal(rc)
print(x)


