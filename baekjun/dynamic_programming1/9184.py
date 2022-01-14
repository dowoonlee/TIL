import sys

abc = list(map(int, sys.stdin.readline().split()))

dp = [[[-1]*21 for _ in range(21)] for _ in range(21)]
for i in range(21):
    for j in range(21):
        dp[i][j][0] = 1
        dp[i][0][j] = 1
        dp[0][i][j] = 1
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i < j and j < k:
                #print(dp[i][j][k-1], dp[i][j-1][k-1], dp[i][j-1][k])
                dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
            else:
                #print(dp[i - 1][j][k] , dp[i - 1][j - 1][k] , dp[i - 1][j][k - 1] , dp[i - 1][j - 1][k - 1])
                dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1]

"""
def w(a, b, c):
    if a<b and b<c:
        if dp[a][b][c-1]<0:
            w(a, b, c-1)
        if dp[a][b-1][c-1]<0:
            w(a, b-1, c-1)
        if dp[a][b-1][c]<0:
            w(a, b-1, c-1)
        dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
    else:
        if dp[a-1][b][c]<0:
            w(a-1, b, c)
        if dp[a-1][b-1][c]<0:
            w(a-1, b-1, c)
        if dp[a-1][b][c-1]<0:
            w(a-1, b, c-1)
        if dp[a-1][b-1][c-1]<0:
            w(a-1, b-1, c-1)
        dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]
    return dp[a][b][c]
"""




    #dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]

    #dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]

while abc != [-1, -1, -1]:
    if abc[0]<=0 or abc[1]<=0 or abc[2]<=0:
        ans = dp[0][0][0]

    elif abc[0]>20 or abc[1]>20 or abc[2]>20:
        ans = dp[20][20][20]
    else:
        ans = dp[abc[0]][abc[1]][abc[2]]

    print('w(%d, %d, %d) = %d'%(abc[0], abc[1], abc[2], ans))
    abc = list(map(int, sys.stdin.readline().split()))

