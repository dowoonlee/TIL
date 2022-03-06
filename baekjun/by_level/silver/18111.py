import sys

n, m, b = map(int, sys.stdin.readline().split())

tile = []



for _ in range(n):
    tile += list(map(int, sys.stdin.readline().split()))

ans = []
heights = []

for h in range(256, -1, -1):
    temp = 0
    usedblock = 0

    for i in range(n*m):
        if tile[i]<h:
            temp += h-tile[i]
            usedblock += h-tile[i]
        else:
            temp += 2*(tile[i]-h)
            usedblock -= (tile[i]-h)
    if usedblock<=b:
        ans.append(temp)
        heights.append(h)


mint = min(ans)
for i in range(len(ans)):
    if ans[i]==mint:
        print(mint, heights[i])
        break




