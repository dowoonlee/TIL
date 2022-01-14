import sys


n1 = int(sys.stdin.readline())
m1 = list(map(int, sys.stdin.readline().split()))
n2 = int(sys.stdin.readline())
m2 = list(map(int, sys.stdin.readline().split()))

def scale(now, left, right, possible):
    new = abs(left - right)
    if (new not in possible):
        possible.append(new)
    if (now == n1):
        return 0
    if not dp[now][new]:
        # 저울의 왼쪽에 놓는경우
        scale(now + 1, left + m1[now], right, possible)
        # 저울의 오른쪽에 놓는경우
        scale(now + 1, left, right + m1[now], possible)
        # 저울에 아예 안놓는경우
        scale(now + 1, left, right, possible)
        dp[now][new] = 1


possible = []
dp = [[0] * (sum(m1) + max(m2)) for _ in range(n1)]

scale(0, 0, 0, possible)

for weight in m2:
    if (weight in possible):
        print("Y", end=' ')
    else:
        print("N", end=' ')





