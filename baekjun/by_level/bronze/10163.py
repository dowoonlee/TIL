import sys

n = int(sys.stdin.readline())
board = [[0]*1001 for _ in range(1001)]

for i in range(1, n+1):
    x, y, w, h = map(int ,sys.stdin.readline().split())

    for dx in range(w):
        for dy in range(h):
            board[x+dx][y+dy] = i

ans = [0]*101
for i in range(1001):
    for j in range(1001):
        if board[i][j]:
            ans[board[i][j]]+=1

for i in range(1, n+1):
    print(ans[i])


