import sys
from collections import deque


t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    D = [0] + list(map(int, sys.stdin.readline().split()))#build time
    s2e = [[] for _ in range(n+1)]#[start_point][end_point]
    dp = [0]*(n+1)#1d dp
    N_end = [0]*(n+1)


    for i in range(k):
        s, e = map(int, sys.stdin.readline().split())
        s2e[s].append(e)
        N_end[e] += 1#N point reach to the [e]
    w = int(sys.stdin.readline())#build_end_point

    q = deque()

    for i in range(1, n+1):
        if not N_end[i]:
            q.append(i)
            dp[i] = D[i]
    while q:
        x = q.popleft()
        for i in s2e[x]:
            N_end[i] -= 1#count 1 direc[some, e]
            dp[i] = max(dp[x] + D[i], dp[i])
            if not N_end[i]:#count all direc heading to [e]
                q.append(i)
    print(dp[w])


