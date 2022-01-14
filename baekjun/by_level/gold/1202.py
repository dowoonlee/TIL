import sys
"""
n , k = map(int, sys.stdin.readline().split())

m, v = [0]*n, [0]*n
for i in range(n):
    m[i], v[i] = map(int, sys.stdin.readline().split())
c = [int(sys.stdin.readline()) for _ in range(k)]
"""

n, k = 3, 2
m, v, c = [1,5,2], [65, 23, 99], [10, 2]


dp = [[0]*(k+1) for _ in range(n)]#dp[i][j] = 처음부터 i번째까지의 물건을 살펴보고, 배낭의 순서 j였을 때 배낭에 들어간 물건의 가치합의 최댓값

for i in range(0, n):#0~i번째 물건
    for j in range(0, n):#c[j]=용량
        if c[j] < m[i]:
            dp[i][j] = dp[i - 1][j]
        else:


