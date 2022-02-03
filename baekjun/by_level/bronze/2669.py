import sys

board = [[0]*101 for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for x in range(x2-x1):
        for y in range(y2-y1):
            board[x+x1+1][y+y1+1] = 1
ans = 0
for i in range(101):
    ans+=sum(board[i])
print(ans)