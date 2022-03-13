import sys

m, n = map(int, sys.stdin.readline().split())
arr = [[0] * n for _ in range(m)]

px, py = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0
cnt = 1
ans = 0
arr[px][py] = 1

while (cnt < m*n):
    nx, ny = px+dx[d], py+dy[d]
    try:
        if (arr[nx][ny]==0):
            px, py = nx, ny
        else:
            if (d==4):
                d =0
            else:
                d+=1
            px += dx[d]
            py += dy[d]
            ans += 1
        arr[px][py] = 1
    except IndexError:
        if (d == 4):
            d = 0
        else:
            d += 1
        px += dx[d]
        py += dy[d]
        arr[px][py] = 1
        ans += 1
    cnt += 1
print(ans)