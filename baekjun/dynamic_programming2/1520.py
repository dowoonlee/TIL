import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def path_finder(x, y):
    if x==m-1 and y==n-1:
        return 1

    if n_path[x][y]!=-1:
        return n_path[x][y]

    n_path[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0<=nx<m) and (0<=ny<n) and (data[nx][ny] < data[x][y]):
            n_path[x][y] += path_finder(nx,ny)

    return n_path[x][y]


m, n = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
n_path = [[-1]*n for _ in range(m)]
print(path_finder(0,0))