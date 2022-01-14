import sys


n = int(sys.stdin.readline())
rgb = [[0]*3 for _ in range(n)]
for i in range(n):
    rgb[i][0], rgb[i][1], rgb[i][2] = map(int, sys.stdin.readline().split())

for i in range(1, n):
    rgb[i][0] += min(rgb[i - 1][1], rgb[i - 1][2])
    rgb[i][1] += min(rgb[i - 1][0], rgb[i - 1][2])
    rgb[i][2] += min(rgb[i - 1][0], rgb[i - 1][1])

print(min(rgb[-1]))
