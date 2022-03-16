import sys

n = int(sys.stdin.readline())

reg = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
init_pos = [0, 0]
q = [init_pos]
dx = [0, 1]
dy = [1, 0]

visited = [[0] * n for _ in range(n)]
visited[0][0] = 1

while q:

    x, y = q[0][0], q[0][1]
    del q[0]

    if reg[x][y] == -1:
        print("HaruHaru")
        break

    else:
        for i in range(2):
            nx = x+dx[i]*reg[x][y]
            ny = y+dy[i]*reg[x][y]

            if nx>=0 and nx<n and ny>=0 and ny<n and visited[nx][ny]==0:
                visited[nx][ny]=1
                q.append([nx, ny])

if visited[-1][-1]==0:
    print("Hing")




