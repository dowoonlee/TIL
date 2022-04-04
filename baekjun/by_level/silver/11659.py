import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
cumsum = [0] * n
cumsum[0] = num[0]


for i in range(1, n):
    cumsum[i] = num[i] + cumsum[i - 1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(cumsum[j - 1])
    else:
        print(cumsum[j - 1] - cumsum[i - 2])
